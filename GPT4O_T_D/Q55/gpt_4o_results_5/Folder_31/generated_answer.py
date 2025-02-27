def lists_with_product_equal_n(circular_list):
    n = 16
    length = len(circular_list)
    circular_list = circular_list + circular_list
    result = []
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= circular_list[j]
            if product == -n:
                result.append(circular_list[i:j + 1])
    return result