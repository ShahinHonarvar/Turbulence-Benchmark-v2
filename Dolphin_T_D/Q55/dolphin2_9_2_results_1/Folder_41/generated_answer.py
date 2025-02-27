def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if product(sublist) == -20:
                result.add(tuple(sublist))
    return [] if not result else [list(t) for t in result]