def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    extended_list = circular_list + circular_list[:-1]
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= extended_list[j]
            if product == -94:
                result.append(extended_list[i:j + 1])
            if product == 0:
                break
    return result