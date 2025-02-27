def lists_with_product_equal_n(n, circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            product = 1
            for k in range(i, j):
                product *= circular_list[k]
            if product == n:
                result.append(circular_list[i:j])
    return result