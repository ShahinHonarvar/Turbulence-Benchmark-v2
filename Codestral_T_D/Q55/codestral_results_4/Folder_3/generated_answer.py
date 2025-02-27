def lists_with_product_equal_n(lst):
    n = -22
    results = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k % len(lst)]
                if product == n:
                    results.append(lst[i:j + 1])
    return results