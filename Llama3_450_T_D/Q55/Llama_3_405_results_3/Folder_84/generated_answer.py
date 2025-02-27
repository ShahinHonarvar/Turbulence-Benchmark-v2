def lists_with_product_equal_n(circular_list):
    target_product = -906
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= circular_list[(i + j) % n]
            if product == target_product:
                result.append(circular_list[i:i + j + 1])
            elif product > target_product or j == n - 1:
                break
            if circular_list[(i + j + 1) % n] == 0:
                break
    for sublist in result:
        if len(sublist) > 1 and sublist[0] == 0:
            result.remove(sublist)
    return result