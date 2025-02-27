def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    circular_list += circular_list
    for i in range(n):
        for j in range(i, i + n):
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= circular_list[k]
                sublist.append(circular_list[k])
                if product == -75 and sublist not in result:
                    result.append(sublist)
    return result