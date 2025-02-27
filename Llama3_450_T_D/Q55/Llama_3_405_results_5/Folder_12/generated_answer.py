def lists_with_product_equal_n(circular_list):
    n = -18
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, i + len(circular_list)):
            product *= circular_list[j % len(circular_list)]
            if product == n:
                result.append(circular_list[i:j + 1])
            elif product > n or j == i + len(circular_list) - 1:
                break
            elif product < n and circular_list[(j + 1) % len(circular_list)] > n // product:
                break
    return result