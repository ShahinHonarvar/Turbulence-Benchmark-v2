def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product > 2:
                break
            if product == 2:
                result.append([lst[(j - k) % n] for k in range(j - i + 1)])
    return result