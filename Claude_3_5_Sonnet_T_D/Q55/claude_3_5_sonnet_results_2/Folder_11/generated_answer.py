def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    extended_list = circular_list * 2
    for i in range(n):
        for j in range(i, i + n):
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= extended_list[k]
                sublist.append(extended_list[k])
                if product == -15:
                    result.append(sublist[:])
                elif product < -15:
                    break
    return result