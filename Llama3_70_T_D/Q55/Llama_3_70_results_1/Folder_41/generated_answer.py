def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -20:
                result.append(lst[(i + j - n + 1) % n:(i + j + 1) % n])
                if j != n - 1:
                    result.append(lst[(i + j + 1) % n:] + lst[:(i + j - n + 1) % n])
    return result