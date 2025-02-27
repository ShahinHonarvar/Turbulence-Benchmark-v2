def lists_with_product_equal_n(circular_list):
    sublists = []
    product = 1
    for i in range(len(circular_list)):
        product *= circular_list[i]
        if product > 51:
            product = 1
            sublists = []
        elif product == 51:
            sublists.append(circular_list[i])
            product = 1
        elif len(sublists) > len(circular_list) // 2:
            sublists = []
        else:
            sublists.append(circular_list[i])
    return sublists