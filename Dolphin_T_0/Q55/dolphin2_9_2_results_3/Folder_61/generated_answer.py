from itertools import combinations

def products_equal_n(lst, n):
    result = []
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length + 1):
            if lst[i:j] not in result and i != j - 1:
                product = 1
                for k in lst[i:j]:
                    product *= k
                if product == n:
                    result.append(lst[i:j])
    return result if result else ['No sublists found']