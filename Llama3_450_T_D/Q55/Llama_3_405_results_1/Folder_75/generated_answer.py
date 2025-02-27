def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == 13:
                result.append([lst[k % n] for k in range(i, j + 1)])
            elif product > 13:
                break
    return result