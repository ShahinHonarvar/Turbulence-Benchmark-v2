def lists_with_product_equal_n(circular_list, n=2):
    if not circular_list:
        return []
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(1, length + 1):
            sublist = []
            product = 1
            for i in range(start, start + end):
                current_index = i % length
                sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
            if product == n:
                result.append(sublist)
    return result