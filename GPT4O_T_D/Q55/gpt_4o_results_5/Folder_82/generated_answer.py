def lists_with_product_equal_n(circular_list):
    n = 8
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        sublist = []
        for i in range(length):
            current = circular_list[(start + i) % length]
            product *= current
            sublist.append(current)
            if product == n:
                result.append(sublist.copy())
            if product == 0 or product > 8:
                break
    return result