def lists_with_product_equal_n(circular_list):
    n = 28
    result = []
    size = len(circular_list)
    for i in range(size):
        product = 1
        sublist = []
        for j in range(i, i + size):
            product *= circular_list[j % size]
            sublist.append(circular_list[j % size])
            if product == n:
                result.append(sublist)
    return result