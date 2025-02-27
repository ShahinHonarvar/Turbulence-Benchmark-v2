def lists_with_product_equal_n(circular_list):
    target_product = -938
    n = len(circular_list)
    result = []
    for start in range(n):
        current_product = 1
        for end in range(start, start + n):
            current_product *= circular_list[end % n]
            if current_product == target_product:
                sublist_length = end - start + 1
                result.append([circular_list[(start + i) % n] for i in range(sublist_length)])
            if sublist_length >= n:
                break
    return result