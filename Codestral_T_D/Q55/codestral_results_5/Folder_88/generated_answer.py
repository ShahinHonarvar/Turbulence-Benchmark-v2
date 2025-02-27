def lists_with_product_equal_n(circular_list):
    n = -56
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        sublist = []
        for j in range(i, i + length):
            product *= circular_list[j % length]
            sublist.append(circular_list[j % length])
            if product == n:
                result.append(sublist)
    return result