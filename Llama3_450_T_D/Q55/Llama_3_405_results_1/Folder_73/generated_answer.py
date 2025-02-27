def lists_with_product_equal_n(circular_list):
    n = 40
    result = []
    list_len = len(circular_list)
    circular_list = circular_list + circular_list
    for i in range(list_len):
        product = 1
        for j in range(i, i + list_len):
            product *= circular_list[j]
            if product == n:
                result.append(circular_list[i:j + 1])
            elif product > n:
                break
    return result