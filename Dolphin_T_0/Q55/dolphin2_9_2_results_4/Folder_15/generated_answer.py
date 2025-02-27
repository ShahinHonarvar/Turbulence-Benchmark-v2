def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            for k in range(i, j + 1):
                product /= lst[k]
                if product == -7:
                    result.append(lst[k:j + 1])
    return result