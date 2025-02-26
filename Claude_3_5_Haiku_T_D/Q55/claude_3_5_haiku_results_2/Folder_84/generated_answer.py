def lists_with_product_equal_n(circular_list):
    n = -906
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(1, length + 1):
            sublist = []
            product = 1
            for i in range(end):
                current_index = (start + i) % length
                current_value = circular_list[current_index]
                sublist.append(current_value)
                product *= current_value
            if product == n:
                result.append(sublist)
    return result