def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                current_element = circular_list[current_index % n]
                sublist.append(current_element)
                product *= current_element
                if product == 33:
                    result.append(sublist.copy())
                    break
                if product > 33:
                    break
                current_index += 1
    return result