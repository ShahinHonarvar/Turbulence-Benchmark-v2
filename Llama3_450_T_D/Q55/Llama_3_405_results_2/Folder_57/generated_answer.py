def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -75
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j % n]
            if product == target_product:
                result.append(circular_list[i:j + 1])
            elif product == 0:
                break
            elif abs(product) > abs(target_product):
                break
    return result