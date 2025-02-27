def lists_with_product_equal_n(circular_list):
    n = -30
    result = []
    length = len(circular_list)
    circular_list += circular_list
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= circular_list[j]
            if product == n:
                result.append(circular_list[i:j + 1])
    return result