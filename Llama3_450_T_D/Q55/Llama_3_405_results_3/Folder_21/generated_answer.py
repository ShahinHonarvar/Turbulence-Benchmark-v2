def lists_with_product_equal_n(lst):
    n = 851
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == n:
                result.append([lst[(i + k) % len(lst)] for k in range(j + 1)])
            elif product > n:
                break
    return result