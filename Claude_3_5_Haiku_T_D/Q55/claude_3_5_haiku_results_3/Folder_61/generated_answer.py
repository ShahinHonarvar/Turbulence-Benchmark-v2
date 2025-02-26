def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_idx = start
            while current_idx <= end:
                current_val = circular_list[current_idx % n]
                sublist.append(current_val)
                product *= current_val
                if product == -10:
                    result.append(sublist.copy())
                    break
                current_idx += 1
    return result