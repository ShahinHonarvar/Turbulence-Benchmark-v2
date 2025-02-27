def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            mod_index = j % n
            sublist.append(circular_list[mod_index])
            product *= circular_list[mod_index]
            if product > 25:
                break
            elif product == 25:
                result.append(sublist[:])
    return result