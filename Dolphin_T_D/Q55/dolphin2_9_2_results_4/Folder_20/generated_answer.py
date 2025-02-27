def lists_with_product_equal_n(lst, n=-69):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i == j:
                continue
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product == n:
                result.append(lst[i:j])
    return result