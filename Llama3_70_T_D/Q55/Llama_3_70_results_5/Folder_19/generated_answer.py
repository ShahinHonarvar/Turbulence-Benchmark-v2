def lists_with_product_equal_n(lst):
    result = set()
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -54:
                result.add(tuple(sorted((lst[(i + k) % n] for k in range(j + 1)))))
    return [list(sublist) for sublist in result]