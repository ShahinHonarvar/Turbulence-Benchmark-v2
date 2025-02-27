def lists_with_product_equal_n(circular_list):
    n = 27
    result = []
    list_size = len(circular_list)
    for i in range(list_size):
        product = 1
        for j in range(list_size):
            product *= circular_list[(i + j) % list_size]
            if product == n:
                result.append(circular_list[i:i + j + 1])
            elif product > n or j == list_size - 1:
                break
    return result