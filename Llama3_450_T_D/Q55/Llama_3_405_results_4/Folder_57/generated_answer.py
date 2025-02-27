def lists_with_product_equal_n(circular_list):
    n = -75
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            product *= circular_list[(i + j) % len(circular_list)]
            if product == n:
                result.append([circular_list[(i + k) % len(circular_list)] for k in range(j + 1)])
            elif product > n:
                break
    return result