def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            if product == 15:
                result.append([circular_list[(i + k) % n] for k in range(j + 1)])
            if product == 0:
                break
    return result