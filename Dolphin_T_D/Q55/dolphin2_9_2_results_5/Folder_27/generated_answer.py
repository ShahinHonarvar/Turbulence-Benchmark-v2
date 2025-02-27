def lists_with_product_equal_n(circular_list):
    result = []
    N = len(circular_list)
    product_map = {}
    prefix_product = 1
    for i in range(2 * N - 1):
        if i < N:
            prefix_product *= circular_list[i]
        if i >= N:
            prefix_product /= circular_list[i - N]
        if prefix_product not in product_map:
            product_map[prefix_product] = 1
        else:
            product_map[prefix_product] += 1
    if -82 in product_map:
        for i in range(N - 1):
            if circular_list[i] * circular_list[i + 1] == -82:
                result.append([circular_list[i], circular_list[i + 1]])
        for i in range(N - 1):
            for j in range(i + 2, N):
                sublist = [circular_list[i]]
                product = circular_list[i]
                for k in range(i + 1, j):
                    product *= circular_list[k]
                    sublist.append(circular_list[k])
                    if product == -82:
                        result.append(sublist)
    return result