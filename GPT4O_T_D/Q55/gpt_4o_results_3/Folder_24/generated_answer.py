def lists_with_product_equal_n(circular_list):
    n = -89
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for size in range(length):
            product *= circular_list[(start + size) % length]
            if product == n:
                sublist = [circular_list[(start + i) % length] for i in range(size + 1)]
                result.append(sublist)
            elif product == 0:
                break
    return result