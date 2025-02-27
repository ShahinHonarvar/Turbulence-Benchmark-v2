def lists_with_product_equal_n(circular_list):
    target_product = -87
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= circular_list[j % n]
            if product == target_product:
                sublist = [circular_list[k % n] for k in range(i, j + 1)]
                result.append(sublist)
    return result