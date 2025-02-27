def lists_with_product_equal_n(circular_list):
    n = -115
    result = []
    list_size = len(circular_list)
    for start_index in range(list_size):
        product = 1
        for end_index in range(start_index, start_index + list_size):
            product *= circular_list[end_index % list_size]
            if product == n:
                sublist = [circular_list[i % list_size] for i in range(start_index, end_index + 1)]
                result.append(sublist)
            elif product == 0 or abs(product) > abs(n):
                break
    return result