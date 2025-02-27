def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k % n]
            if product == -51:
                result.append(lst[i:j + 1])
    return result