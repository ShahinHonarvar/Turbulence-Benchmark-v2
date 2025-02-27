def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(1, n + 1):
            k = (i + j - 1) % n
            product *= lst[k]
            if product == 6:
                result.append([lst[(i + m - 1) % n] for m in range(1, j + 1)])
    return result