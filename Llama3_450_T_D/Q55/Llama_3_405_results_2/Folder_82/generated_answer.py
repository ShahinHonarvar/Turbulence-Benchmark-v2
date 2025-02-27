def lists_with_product_equal_n(circular_list):
    n = 8
    result = []
    list_len = len(circular_list)
    for start in range(list_len):
        product = 1
        for end in range(start, start + list_len):
            product *= circular_list[end % list_len]
            if product == n:
                result.append(circular_list[start:end + 1])
            elif product > n:
                break
    return result