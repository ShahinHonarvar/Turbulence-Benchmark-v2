def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            if i == j:
                continue
            product = 1
            for k in range(i, j + 1):
                product *= lst[k % n]
            if product == 85:
                result.append(lst[i:j + 1])
    return result