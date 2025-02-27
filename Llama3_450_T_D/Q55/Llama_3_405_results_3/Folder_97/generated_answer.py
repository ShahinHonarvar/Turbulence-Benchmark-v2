def lists_with_product_equal_n(circular_list):
    n = -938
    result = []
    list_size = len(circular_list)
    for start_index in range(list_size):
        product = 1
        for end_index in range(start_index, start_index + list_size):
            end_index %= list_size
            product *= circular_list[end_index]
            if product == n:
                result.append(circular_list[start_index:end_index + 1])
            elif product == 0 or abs(product) > abs(n):
                break
    return result