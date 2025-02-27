def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            idx = (i + j) % n
            product *= circular_list[idx]
            if product == 43 and j < n:
                sublist = [circular_list[(i + k) % n] for k in range(j + 1)]
                result.append(sublist)
    return result