def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    product = 1
    sublist = []
    result = []
    for i in range(n):
        product *= circular_list[i]
        sublist.append(circular_list[i])
        if product == -56:
            result.append(sublist[:])
        while product > 1 and len(sublist) > 1:
            product /= sublist.pop(0)
            if product == -56:
                result.append(sublist[:])
    return result