def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []
    for i in range(size):
        product = 1
        sublist = []
        for j in range(i, size + i):
            product *= circular_list[j % size]
            sublist.append(circular_list[j % size])
            if product == -56:
                result.append(sublist)
            if product != 0 and -56 % product != 0:
                break
    return result