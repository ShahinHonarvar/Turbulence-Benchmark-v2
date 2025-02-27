def lists_with_product_equal_n(l):
    result = []
    l = l + l
    n = len(l)
    for i in range(n):
        for j in range(i + 2, n + i + 1):
            product = 1
            for k in range(i, j):
                product *= l[k]
            if product == 3:
                result.append(l[i:j])
    return result