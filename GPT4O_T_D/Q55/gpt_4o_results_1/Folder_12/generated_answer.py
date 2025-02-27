def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            current_index = (start + i) % n
            sublist.append(circular_list[current_index])
            product *= circular_list[current_index]
            if product == -18:
                result.append(sublist[:])
        del sublist[:]
    return result