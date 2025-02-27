def lists_with_product_equal_n(circular_list):
    n = -16
    result = []
    list_size = len(circular_list)
    for i in range(list_size):
        product = 1
        for j in range(i, list_size + i):
            product *= circular_list[j % list_size]
            if product == n:
                result.append(circular_list[i:j % list_size + 1])
            if product == 0:
                break
    return result