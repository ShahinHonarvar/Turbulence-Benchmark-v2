def lists_with_product_equal_n(circular_list):
    n = -57
    result = []
    list_size = len(circular_list)
    for i in range(list_size):
        product = 1
        for j in range(i, list_size + i):
            product *= circular_list[j % list_size]
            if product == n:
                result.append(circular_list[i:j + 1])
            elif product > n or j >= list_size + i - 1:
                break
    return result