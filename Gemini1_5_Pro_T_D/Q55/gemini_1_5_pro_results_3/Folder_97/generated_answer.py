def lists_with_product_equal_n(circular_list):
    n = -938
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        for j in range(len(circular_list)):
            index = (i + j) % len(circular_list)
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist.copy())
    return result