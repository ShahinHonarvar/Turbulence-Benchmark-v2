def lists_with_product_equal_n(lst):
    product = 1
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst) - i):
            sublist = lst[(i + j) % len(lst)]
            product *= sublist
            if product == 6:
                result.append(sublist)
    return result