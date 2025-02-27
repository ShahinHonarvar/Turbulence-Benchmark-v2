def lists_with_product_equal_n(circular_list):
    n = -5
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= circular_list[j % length]
            if product == n:
                result.append(circular_list[i:j + 1])
            if product > abs(n) and n < 0 or (product < -abs(n) and n > 0):
                break
    return result