def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length) % n
            product *= circular_list[end]
            if product == 47:
                result.append(circular_list[start:start + length])
            elif product > 47:
                break
    return result