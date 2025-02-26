def lists_with_product_equal_n(circular_list):
    n = -18
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                curr_index = i % length
                curr_value = circular_list[curr_index]
                sublist.append(curr_value)
                product *= curr_value
            if product == n:
                result.append(sublist)
    return result