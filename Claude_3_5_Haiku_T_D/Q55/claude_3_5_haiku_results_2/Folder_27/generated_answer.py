def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                sublist.append(circular_list[current_index % n])
                product *= circular_list[current_index % n]
                current_index += 1
                if product == -82:
                    result.append(sublist.copy())
    return result