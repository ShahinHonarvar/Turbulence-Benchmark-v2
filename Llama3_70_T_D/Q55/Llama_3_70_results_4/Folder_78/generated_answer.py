def lists_with_product_equal_n(lst):
    n = len(lst)
    result = set()
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product > 74:
                break
            if product == 74:
                result.add(tuple(sorted((lst[(i + k) % n] for k in range(j + 1)))))
    return [list(t) for t in result]