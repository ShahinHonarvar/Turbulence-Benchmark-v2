def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            product = 1
            for i in range(length):
                curr_index = (start + i) % n
                curr_element = circular_list[curr_index]
                sublist.append(curr_element)
                product *= curr_element
            if product == 76:
                result.append(sublist)
    return result