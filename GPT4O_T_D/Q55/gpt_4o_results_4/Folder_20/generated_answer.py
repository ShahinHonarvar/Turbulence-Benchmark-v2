def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == -69:
                sublist = [circular_list[(i + k) % n] for k in range(j + 1)]
                result.append(sublist)
            if abs(product) > abs(-69) and product != 0:
                break
    return result