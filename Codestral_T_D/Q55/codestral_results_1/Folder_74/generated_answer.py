def lists_with_product_equal_n(lst):
    lst *= 2
    n = len(lst)
    result = []
    for i in range(n):
        p = 1
        for j in range(i, n):
            p *= lst[j]
            if p == 51:
                result.append(lst[i:j + 1])
    return result