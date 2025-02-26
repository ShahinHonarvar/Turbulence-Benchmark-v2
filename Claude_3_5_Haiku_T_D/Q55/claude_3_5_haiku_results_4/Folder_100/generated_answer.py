def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                current_element = circular_list[current_index % n]
                sublist.append(current_element)
                product *= current_element
                if product == 48:
                    result.append(sublist.copy())
                    break
                if product > 48:
                    break
                current_index += 1
    return result