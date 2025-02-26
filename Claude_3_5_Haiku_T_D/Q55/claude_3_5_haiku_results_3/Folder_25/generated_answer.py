def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                idx = current_index % n
                sublist.append(circular_list[idx])
                product *= circular_list[idx]
                current_index += 1
                if product == -32:
                    result.append(sublist.copy())
    return result