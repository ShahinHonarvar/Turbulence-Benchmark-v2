def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j + 1]
            product = 1
            for k in sublist:
                product *= k
            if product == -33:
                result.append(sublist)
    return result