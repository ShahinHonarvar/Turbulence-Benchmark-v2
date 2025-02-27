def lists_with_product_equal_n(circular_list):
    n = 100
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            product *= circular_list[(i + j) % len(circular_list)]
            if product == n:
                result.append(circular_list[i:i + j + 1])
            elif product > n:
                break
            if (i + j + 1) % len(circular_list) == 0 and product < n:
                break
    return result