def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    extended_list = circular_list * 2
    for i in range(n):
        product = 1
        for j in range(n):
            product *= extended_list[i + j]
            if product == -30:
                results.append(extended_list[i:i + j + 1])
    return results