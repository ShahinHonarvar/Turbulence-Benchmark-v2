def lists_with_product_equal_n(circular_list):
    n = 13
    result = []
    for i in range(len(circular_list)):
        prod = 1
        sublist = []
        for j in range(i, i + len(circular_list)):
            index = j % len(circular_list)
            prod *= circular_list[index]
            sublist.append(circular_list[index])
            if prod == n:
                result.append(sublist)
            if prod > n:
                break
    return result