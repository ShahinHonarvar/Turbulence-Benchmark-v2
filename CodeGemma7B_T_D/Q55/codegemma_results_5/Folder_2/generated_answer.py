def lists_with_product_equal_n(a):
    n = -968
    res = []
    prod = 1
    start = 0
    for i in range(len(a)):
        prod *= a[i]
        while prod >= n:
            if prod == n:
                res.append(a[start:i + 1])
            prod //= a[start]
            start += 1
    return res