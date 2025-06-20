def lists_with_product_equal_n(circular_list):
    n = -94
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list) + i):
            product *= circular_list[j % len(circular_list)]
            if product == n:
                result.append([circular_list[k % len(circular_list)] for k in range(i, j + 1)])
            elif product > abs(n):
                break
    return result