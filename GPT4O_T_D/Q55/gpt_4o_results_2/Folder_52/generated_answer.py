def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == 37:
                result.append([circular_list[i % n] for i in range(start, end + 1)])
            if product == 0 or abs(product) > 37:
                break
    return result