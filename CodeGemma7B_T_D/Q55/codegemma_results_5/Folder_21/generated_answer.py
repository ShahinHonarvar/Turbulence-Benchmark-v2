def lists_with_product_equal_n(circular_list):
    product_0 = 1
    product_1 = 1
    zero_count = 0
    negative_count = 0
    list_with_product_n = []
    for num in circular_list + circular_list:
        if num == 0:
            zero_count += 1
            if product_0 != 0:
                list_with_product_n.append(circular_list)
            product_0 = 1
        if num < 0:
            negative_count += 1
        else:
            product_0 *= num
        if zero_count == 1 and negative_count % 2 == 0:
            list_with_product_n.append(circular_list)
        if zero_count > 1 and negative_count % 2 == 0:
            product_1 *= num
        if zero_count == 1 and negative_count % 2 == 1:
            if product_1 != 0:
                list_with_product_n.append(circular_list)
            product_1 = 1
        if zero_count > 1 and negative_count % 2 == 1:
            if product_1 != 0:
                list_with_product_n.append(circular_list)
            product_1 = 1
    return list_with_product_n