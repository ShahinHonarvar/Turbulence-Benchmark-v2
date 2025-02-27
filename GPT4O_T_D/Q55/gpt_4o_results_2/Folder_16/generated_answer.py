def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for end in range(start, start + n):
            idx = end % n
            sublist.append(circular_list[idx])
            product *= circular_list[idx]
            if product == -837:
                result.append(sublist.copy())
            if abs(product) > abs(-837):
                break
    return result