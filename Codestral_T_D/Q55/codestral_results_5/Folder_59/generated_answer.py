def lists_with_product_equal_n(circular_list):
    n = -3
    result = []
    size = len(circular_list)
    circular_list += circular_list
    for i in range(size):
        for j in range(i + 1, i + size):
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= circular_list[k]
                sublist.append(circular_list[k])
                if product == n:
                    result.append(sublist)
    return result