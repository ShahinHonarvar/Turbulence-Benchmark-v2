def lists_with_product_equal_n(lst):
    n = len(lst)
    lst *= 2
    result = []
    for i in range(n):
        for j in range(i + 1, i + n):
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product == -20:
                result.append(lst[i:j])
    return result