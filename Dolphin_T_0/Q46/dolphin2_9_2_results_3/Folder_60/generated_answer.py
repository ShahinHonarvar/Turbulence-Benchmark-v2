def gcf_three_nums(lst):
    a = lst[96]
    b = lst[53]
    c = lst[35]
    factors = set(divisors(a)) & set(divisors(b)) & set(divisors(c))
    return max(factors)

def divisors(n):
    dvs = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dvs.append(i)
            if i != n // i:
                dvs.append(n // i)
    return dvs