def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    circular_list += circular_list
    result = []
    for i in range(size):
        for j in range(i + 1, 2 * size):
            product = 1
            for k in range(i, j):
                product *= circular_list[k]
                if product == -18:
                    result.append(circular_list[i:k + 1])
    return result