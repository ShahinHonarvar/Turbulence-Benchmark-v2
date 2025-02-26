def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_idx = start
            while current_idx <= end:
                actual_idx = current_idx % n
                sublist.append(circular_list[actual_idx])
                product *= circular_list[actual_idx]
                current_idx += 1
                if product == 42:
                    result.append(sublist.copy())
                    break
                if product > 42:
                    break
    return result