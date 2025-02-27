def lists_with_product_equal_n(circular_list):
    n = -15
    result = []
    list_len = len(circular_list)
    for i in range(list_len):
        product = 1
        for j in range(i, list_len + i):
            product *= circular_list[j % list_len]
            if product == n:
                sublist = [circular_list[k % list_len] for k in range(i, j + 1)]
                result.append(sublist)
            elif product == 0:
                break
    return result