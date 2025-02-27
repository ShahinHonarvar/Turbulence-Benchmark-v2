def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -22:
                result.append(lst[(i + j) % n:(i + j + 1) % n] if j != 0 else lst)
    return result