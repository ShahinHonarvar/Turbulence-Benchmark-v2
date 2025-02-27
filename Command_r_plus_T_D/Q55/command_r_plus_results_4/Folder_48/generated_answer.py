def lists_with_product_equal_n(circular_list):
    n = 990
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and reduce(lambda x, y: x * y, sublist, 1) == n:
                result.append(sublist)
    return result