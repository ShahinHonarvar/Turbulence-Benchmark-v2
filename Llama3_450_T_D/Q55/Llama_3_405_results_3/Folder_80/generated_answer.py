def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == 43:
                result.append([lst[(i + k) % n] for k in range(j + 1)])
            elif product > 43:
                break
    return result