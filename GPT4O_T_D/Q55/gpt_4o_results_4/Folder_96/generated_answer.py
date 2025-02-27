def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        prod = 1
        sublist = []
        for end in range(start, start + n):
            index = end % n
            prod *= circular_list[index]
            sublist.append(circular_list[index])
            if prod == 0:
                result.append(sublist.copy())
    return result