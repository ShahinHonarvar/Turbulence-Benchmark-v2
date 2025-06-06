def lists_with_product_equal_n(circular_list):
    n = 28
    result = []
    length = len(circular_list)
    for i in range(length):
        product = 1
        for j in range(i, length + i):
            product *= circular_list[j % length]
            if product == n:
                result.append(circular_list[i:j % length + 1])
            elif product > n:
                break
    return result