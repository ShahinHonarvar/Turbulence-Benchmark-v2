def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for end in range(n):
            product *= circular_list[(start + end) % n]
            if product == 93:
                result.append(circular_list[start:start + end + 1])
            elif product > 93:
                break
    return result