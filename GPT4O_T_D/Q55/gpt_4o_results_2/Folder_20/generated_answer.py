def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    extended_list = circular_list + circular_list
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= extended_list[end]
            if product == -69:
                result.append(extended_list[start:end + 1])
            if abs(product) > abs(-69):
                break
    return result