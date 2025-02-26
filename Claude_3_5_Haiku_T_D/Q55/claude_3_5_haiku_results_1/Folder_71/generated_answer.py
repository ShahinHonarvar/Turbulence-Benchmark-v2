def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                curr_val = circular_list[current_index % n]
                product *= curr_val
                sublist.append(curr_val)
                if product == 47:
                    result.append(sublist.copy())
                    break
                if product > 47:
                    break
                current_index += 1
    return result