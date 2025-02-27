def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n - 1):
            product *= lst[(i + j) % n]
            if product == 27:
                result.append([lst[(i + k) % n] for k in range(j + 1)])
            elif product > 27:
                break
    if product == 27:
        result.append(lst)
    return result