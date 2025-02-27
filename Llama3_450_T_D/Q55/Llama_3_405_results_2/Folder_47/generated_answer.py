def lists_with_product_equal_n(circular_list):
    n = -94
    result = []
    list_length = len(circular_list)
    circular_list += circular_list
    for i in range(list_length):
        product = 1
        for j in range(i, i + list_length):
            product *= circular_list[j]
            if product == n:
                result.append(circular_list[i:j + 1])
            elif product == 0 or abs(product) > abs(n):
                break
    return result