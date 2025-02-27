def lists_with_product_equal_n(circular_list):
    n = 37
    result = []
    list_size = len(circular_list)
    for start in range(list_size):
        product = 1
        for end in range(start, start + list_size):
            product *= circular_list[end % list_size]
            if product == n:
                result.append(circular_list[start:end + 1])
            elif product > n or end == start + list_size - 1:
                break
    return result