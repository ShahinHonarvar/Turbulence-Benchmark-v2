def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == 13:
                result.append(lst[(i + j) % len(lst)])
            elif product > 13:
                break
    return result