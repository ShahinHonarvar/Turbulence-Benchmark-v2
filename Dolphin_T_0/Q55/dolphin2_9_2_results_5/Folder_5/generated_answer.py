def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == -33:
                result.append(lst[(i + j) % len(lst)])
        if len(result) > 0:
            return result
    return []