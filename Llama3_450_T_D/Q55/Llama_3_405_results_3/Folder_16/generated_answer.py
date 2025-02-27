def lists_with_product_equal_n(circular_list):
    target_product = -837
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == target_product:
                result.append(circular_list[i:i + j + 1] if i + j + 1 <= n else circular_list[i:] + circular_list[:i + j + 1 - n])
            if product == 0:
                break
            if abs(product) > abs(target_product):
                break
    return result