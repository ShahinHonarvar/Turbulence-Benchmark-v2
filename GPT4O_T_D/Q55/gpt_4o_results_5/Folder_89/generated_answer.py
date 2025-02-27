def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            if product == 57:
                sublist = [circular_list[(i + k) % n] for k in range(j + 1)]
                result.append(sublist)
            if product == 0 or product > 57:
                break
    return result