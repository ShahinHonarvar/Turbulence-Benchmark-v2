def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            j_real = j % n
            if j_real == i:
                break
            product = 1
            for k in range(i, j_real):
                k_real = k % n
                product *= lst[k_real]
            if product == -65:
                result.append([lst[k % n] for k in range(i, j_real)])
    return result