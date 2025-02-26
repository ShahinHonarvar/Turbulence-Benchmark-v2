def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            current_sublist = []
            current_product = 1
            idx = start
            while idx <= end:
                current_sublist.append(circular_list[idx % n])
                current_product *= circular_list[idx % n]
                if current_product == 76:
                    result.append(current_sublist.copy())
                    break
                if current_product > 76:
                    break
                idx += 1
    return result