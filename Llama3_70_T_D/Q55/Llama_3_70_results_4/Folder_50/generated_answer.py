def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product > 45:
                break
            elif product == 45:
                result.append(lst[(i + j + 1) % len(lst):] + lst[:(i + j + 1) % len(lst)][::-1])
    return [sublist for sublist in result if len(sublist) <= len(lst)]