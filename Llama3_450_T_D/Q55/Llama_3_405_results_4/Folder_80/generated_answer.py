def lists_with_product_equal_n(circular_list):
    target_product = 43
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == target_product:
                sublist = [circular_list[(i + k) % n] for k in range(j + 1)]
                result.append(sublist)
            elif product > target_product:
                break
    return result