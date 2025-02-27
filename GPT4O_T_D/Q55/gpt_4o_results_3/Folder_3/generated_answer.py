def lists_with_product_equal_n(c_list):
    n = len(c_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            product *= c_list[(start + length - 1) % n]
            if product == -22:
                end = (start + length) % n
                if end > start:
                    result.append(c_list[start:end])
                else:
                    result.append(c_list[start:] + c_list[:end])
    return result