def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = []
            product = 1
            for i in range(end):
                current_index = (start + i) % n
                current_value = circular_list[current_index]
                sublist.append(current_value)
                product *= current_value
            if product == -17:
                result.append(sublist)
    return result