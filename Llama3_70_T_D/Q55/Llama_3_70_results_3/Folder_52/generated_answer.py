def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product > 37:
                break
            if product == 37:
                result.append([lst[(i + k) % len(lst)] for k in range(j + 1)])
    return result