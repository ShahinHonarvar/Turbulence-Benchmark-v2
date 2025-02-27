def lists_with_product_equal_n(circular_list):
    n = -56
    result = []
    list_length = len(circular_list)
    for i in range(list_length):
        product = 1
        for j in range(i, list_length + i):
            product *= circular_list[j % list_length]
            if product == n:
                result.append(circular_list[i:j % list_length + 1])
            elif product > n or j == list_length + i - 1:
                break
    return result