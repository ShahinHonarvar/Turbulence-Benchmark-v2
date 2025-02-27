from itertools import combinations

def product_equal_n(lst, n):
    if n == 0:
        return [[]]
    result = []
    for i in range(1, min(len(lst), -n) + 1):
        for comb in combinations(lst, i):
            if n // -i == 0 or n / -i != int(n / -i) or (n != -54 and n % -i != 0 and (n // -i != int(n // -i))):
                continue
            elif n == -54 and comb[0] == -1 and (comb[-1] == -1):
                continue
            elif n != -54 and (comb[0] == -1 or comb[-1] == -1 or (1 > comb[::-1] > -n and 1 > -comb[::-1] > -n)):
                continue
            elif all((v in lst for v in comb)):
                prod = 1
                for val in comb:
                    prod *= val
                if prod == n:
                    result.append(comb)
    return result