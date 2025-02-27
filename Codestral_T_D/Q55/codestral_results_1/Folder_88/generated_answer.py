def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    circular_list += circular_list
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            product = 1
            for k in range(i, j):
                product *= circular_list[k]
                if product == -56:
                    result.append(circular_list[i:j])
    return result