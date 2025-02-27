def lists_with_product_equal_n(circular_list):
    n = -54
    result = []
    list_size = len(circular_list)
    for start in range(list_size):
        product = 1
        for end in range(start, list_size + start):
            product *= circular_list[end % list_size]
            if product == n:
                result.append(circular_list[start:end + 1])
            elif product > n or end == list_size + start - 1:
                break
    return result