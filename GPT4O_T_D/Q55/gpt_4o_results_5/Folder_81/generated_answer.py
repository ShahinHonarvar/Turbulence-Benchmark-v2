def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == -8:
                if (i + j) % n >= i:
                    result.append(circular_list[i:(i + j) % n + 1])
                else:
                    result.append(circular_list[i:] + circular_list[:(i + j) % n + 1])
    return result if result else []