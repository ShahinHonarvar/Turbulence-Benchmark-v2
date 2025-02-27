def lists_with_product_equal_n(circular_list):
    n = -16
    result = []
    length = len(circular_list)
    circular_list += circular_list[:-1]
    for i in range(length):
        for j in range(i, length + i):
            product = 1
            for k in range(i, j + 1):
                product *= circular_list[k]
                if product == n:
                    result.append(circular_list[i:k + 1])
    return result