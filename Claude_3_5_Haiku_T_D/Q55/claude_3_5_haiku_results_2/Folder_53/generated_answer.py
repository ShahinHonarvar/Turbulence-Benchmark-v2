def lists_with_product_equal_n(circular_list):
    n = -87
    length = len(circular_list)
    result = []
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % length
                current_value = circular_list[current_index]
                sublist.append(current_value)
                product *= current_value
            if product == n:
                result.append(sublist)
    return result