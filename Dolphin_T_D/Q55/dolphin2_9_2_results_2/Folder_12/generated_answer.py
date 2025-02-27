def lists_with_product_equal_n(l, n):
    results = []
    size = len(l)
    product = 1
    for i in range(size):
        product *= l[i]
    if product != n:
        return []
    else:
        for i in range(size):
            for j in range(i + 2, size + 1):
                product = 1
                for k in range(i, j):
                    product *= l[k]
                if product == n:
                    results.append(l[i:j])
    return results