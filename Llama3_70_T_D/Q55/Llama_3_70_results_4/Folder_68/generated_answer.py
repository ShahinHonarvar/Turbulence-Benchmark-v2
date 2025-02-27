def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product > 6:
                break
            if product == 6:
                result.append([lst[(j - k) % n] for k in range(j - i + 1)])
    return result