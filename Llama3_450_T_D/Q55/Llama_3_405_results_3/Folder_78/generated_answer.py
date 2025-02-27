def lists_with_product_equal_n(circular_list):
    n = 74
    result = []
    list_size = len(circular_list)
    for i in range(list_size):
        product = 1
        for j in range(i, i + list_size):
            product *= circular_list[j % list_size]
            if product == n:
                sublist = [circular_list[k % list_size] for k in range(i, j + 1)]
                result.append(sublist)
            elif product > n:
                break
    return result