def lists_with_product_equal_n(lst):
    result = []
    product = 1
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == 49:
                result.append(lst[(i + j + 1 - len(lst)) % len(lst):i + j + 1])
    return result