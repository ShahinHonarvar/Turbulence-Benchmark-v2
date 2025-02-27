def lists_with_product_equal_n(circular_list):
    n = 6
    result = []
    length = len(circular_list)
    extended_list = circular_list + circular_list[:-1]
    for start in range(length):
        product = 1
        sublist = []
        for i in range(length):
            current_index = start + i
            product *= extended_list[current_index]
            sublist.append(extended_list[current_index])
            if product == n:
                result.append(sublist[:])
            elif product > n or current_index - start + 1 == length:
                break
    return result