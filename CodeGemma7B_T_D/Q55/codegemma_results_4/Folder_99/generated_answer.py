def lists_with_product_equal_n(circular_list):
    list_size = len(circular_list)
    for i in range(list_size):
        prod = circular_list[i]
        for j in range(i + 1, list_size):
            prod *= circular_list[j]
            if prod == 415:
                sublist = []
                for k in range(i, j + 1):
                    sublist.append(circular_list[k])
                return sublist
    return []