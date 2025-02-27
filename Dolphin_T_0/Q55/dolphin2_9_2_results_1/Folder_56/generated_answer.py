def lists_with_product_equal_n(l):
    n = len(l)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= l[j % n]
            if i != j % n and product == -65:
                result.append(l[i:j % n + 1])
    return result