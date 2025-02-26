def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                curr_index = i % n
                curr_val = circular_list[curr_index]
                sublist.append(curr_val)
                product *= curr_val
            if product == -54:
                result.append(sublist)
    return result