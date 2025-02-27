def lists_with_product_equal_n(circular_list):
    target_product = 96
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == target_product:
                result.append(circular_list[i:i + j + 1])
            elif product > target_product or j == n - 1:
                break
    return result