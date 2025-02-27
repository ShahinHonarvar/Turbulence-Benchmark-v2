def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for offset in range(n):
            index = (start + offset) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == -97:
                result.append(sublist[:])
            if abs(product) > abs(-97):
                break
    return result