def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    circular_list += circular_list
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == -54:
                result.append(sublist)
            if product == 0:
                break
    return result