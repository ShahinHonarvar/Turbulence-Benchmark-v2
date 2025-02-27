def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -83
    result = []
    for i in range(n):
        product = 1
        for j in range(1, n + 1):
            idx = (i + j - 1) % n
            product *= circular_list[idx]
            if product == target_product:
                sublist = [circular_list[(i + k) % n] for k in range(j)]
                result.append(sublist)
            elif product == 0:
                break
    return result