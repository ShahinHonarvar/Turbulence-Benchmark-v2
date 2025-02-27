def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(n):
            idx = (i + j) % n
            product *= circular_list[idx]
            if product == -95:
                sublist_length = j + 1
                sublist = []
                for k in range(sublist_length):
                    sublist.append(circular_list[(i + k) % n])
                result.append(sublist)
            elif product == 0:
                break
    return result