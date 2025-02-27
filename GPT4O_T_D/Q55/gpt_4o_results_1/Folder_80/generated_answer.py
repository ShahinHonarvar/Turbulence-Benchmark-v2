def lists_with_product_equal_n(circular_list):
    n = 43
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for sublist_size in range(1, length + 1):
            end = (start + sublist_size - 1) % length
            product *= circular_list[end]
            if sublist_size > 1 and end == start:
                break
            if product == n:
                if start <= end:
                    result.append(circular_list[start:end + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:end + 1])
    return result