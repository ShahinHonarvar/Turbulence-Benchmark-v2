def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n):
            sublist = circular_list[i:j + 1]
            if j - i + 1 < n and math.prod(sublist) == -95:
                result.append(sublist)
            if i != 0:
                sublist = circular_list[i:] + circular_list[:j + 1 - n]
                if math.prod(sublist) == -95:
                    result.append(sublist)
    return result