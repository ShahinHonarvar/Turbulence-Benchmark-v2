def lists_with_product_equal_n(lst):
    result = set()
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -15:
                result.add(tuple((lst[(i + k) % n] for k in range(j + 1))))
    return [list(sublist) for sublist in result]