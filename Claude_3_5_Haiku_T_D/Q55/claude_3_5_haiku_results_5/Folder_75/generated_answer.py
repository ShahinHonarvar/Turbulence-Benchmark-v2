def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            curr_index = start
            while curr_index <= end:
                curr_elem = circular_list[curr_index % n]
                sublist.append(curr_elem)
                product *= curr_elem
                if product == 13:
                    result.append(sublist.copy())
                    break
                curr_index += 1
    return result