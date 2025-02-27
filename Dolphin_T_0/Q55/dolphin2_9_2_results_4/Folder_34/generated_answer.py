def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= circular_list[j]
            if product == -81:
                result.append(circular_list[i:j + 1])
    return result