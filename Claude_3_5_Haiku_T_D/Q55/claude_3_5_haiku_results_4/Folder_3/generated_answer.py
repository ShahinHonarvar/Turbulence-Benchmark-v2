def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            current_product = 1
            for i in range(start, end + 1):
                current_index = i % n
                current_element = circular_list[current_index]
                sublist.append(current_element)
                current_product *= current_element
            if current_product == -22 and len(sublist) > 0:
                result.append(sublist)
    return result