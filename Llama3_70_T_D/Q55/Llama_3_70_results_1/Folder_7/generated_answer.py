def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product > 537:
                break
            if product == 537:
                result.append((lst[(i + j) % n] for _ in range(j + 1)))
    return result