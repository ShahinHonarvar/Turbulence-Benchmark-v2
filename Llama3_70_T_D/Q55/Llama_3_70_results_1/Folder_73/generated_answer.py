def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == 40:
                result.append(lst[(i + j - n + 1) % n:(i + j + 1) % n])
    return result