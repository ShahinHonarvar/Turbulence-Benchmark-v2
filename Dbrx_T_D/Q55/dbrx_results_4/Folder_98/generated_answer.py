def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublst = []
        product = 1
        for j in range(i, len(lst)):
            sublst.append(lst[j])
            product *= lst[j]
            if product == -1:
                result.append(sublst.copy())
            elif product > 0:
                break
    return result