def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            current_sublist = []
            product = 1
            for i in range(length):
                current_index = (start + i) % n
                current_sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
            if product == -82:
                result.append(current_sublist)
    return result