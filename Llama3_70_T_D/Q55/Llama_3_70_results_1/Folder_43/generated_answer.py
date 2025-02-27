def lists_with_product_equal_n(lst):
    n = len(lst)
    result = set()
    for i in range(n):
        product = 1
        for j in range(1, n + 1):
            product *= lst[(i + j - 1) % n]
            if product == -26:
                result.add(tuple((lst[(i + k - 1) % n] for k in range(j))))
    return [list(sublist) for sublist in result]