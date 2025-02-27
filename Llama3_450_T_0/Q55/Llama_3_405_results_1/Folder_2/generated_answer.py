def lists_with_product_equal_n(circular_list):
    target_product = -968
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == target_product:
                result.append(circular_list[i:i + j + 1])
            elif product > abs(target_product):
                break
    return result