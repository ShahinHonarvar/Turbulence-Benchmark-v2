def lists_with_product_equal_n(circular_list):
    n = -83
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(length):
            product *= circular_list[(i + j) % length]
            if product == n:
                result.append(circular_list[i:i + j + 1])
            elif product == 0 or abs(product) > abs(n):
                break
    return result