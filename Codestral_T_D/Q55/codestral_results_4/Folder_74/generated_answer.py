def lists_with_product_equal_n(circular_list):
    n = 51
    result = []
    for i in range(len(circular_list)):
        prod = 1
        sublist = []
        for j in range(i, len(circular_list) + i):
            k = j % len(circular_list)
            prod *= circular_list[k]
            sublist.append(circular_list[k])
            if prod == n:
                result.append(sublist)
            if prod > n:
                break
    return result