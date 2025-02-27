def lists_with_product_equal_n(circular_list):
    n = -20
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list) + i):
            product *= circular_list[j % len(circular_list)]
            if product == n:
                result.append(circular_list[i:j + 1])
            elif product > abs(n) and n < 0 or (product < n and n > 0):
                break
    return result