def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:2]
    result = set()
    for i in range(n):
        p = 1
        for j in range(i, n + i):
            p *= lst[j]
            if p == -75:
                result.add(tuple(lst[i:j + 1]))
    return list(result)