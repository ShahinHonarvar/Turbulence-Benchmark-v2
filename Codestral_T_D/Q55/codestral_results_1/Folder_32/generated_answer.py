def lists_with_product_equal_n(circular_list):
    n = 76
    result = []
    length = len(circular_list)
    circular_list = circular_list + circular_list
    for i in range(length):
        for j in range(i, i + length):
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= circular_list[k]
                sublist.append(circular_list[k])
                if product == n:
                    result.append(sublist)
                elif product > n:
                    break
    return result