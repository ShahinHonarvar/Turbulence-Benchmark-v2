def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            sublist = circular_list[i:j]
            product = 1
            for k in sublist:
                product *= k
            if product == -968:
                result.append(sublist)
    return result