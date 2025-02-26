def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            product = 1
            sublist = []
            for i in range(length):
                current_index = (start + i) % n
                product *= circular_list[current_index]
                sublist.append(circular_list[current_index])
            if product == -46:
                result.append(sublist)
    return result