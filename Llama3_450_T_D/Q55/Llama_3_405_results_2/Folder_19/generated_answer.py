def lists_with_product_equal_n(circular_list):
    n = -54
    result = []
    list_size = len(circular_list)
    for i in range(list_size):
        product = 1
        for j in range(i, i + list_size):
            product *= circular_list[j % list_size]
            if product == n:
                result.append(circular_list[i:j + 1])
            if product > n or j == i + list_size - 1:
                break
            if circular_list[(j + 1) % list_size] == 0:
                break
    return result