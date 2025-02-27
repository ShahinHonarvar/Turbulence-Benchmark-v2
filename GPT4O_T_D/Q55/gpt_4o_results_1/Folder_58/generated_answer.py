def lists_with_product_equal_n(circular_list):
    n = 733
    length = len(circular_list)
    result = []
    for i in range(length):
        product = 1
        for j in range(length):
            product *= circular_list[(i + j) % length]
            if product == n:
                sublist = [circular_list[(i + k) % length] for k in range(j + 1)]
                result.append(sublist)
            if product == 0 or product > n:
                break
    return result