def lists_with_product_equal_n(circular_list):
    n = 36
    result = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i, size):
            sub_list = circular_list[i:j + 1]
            if i > j:
                sub_list = circular_list[i:] + circular_list[:j + 1]
            product = 1
            for x in sub_list:
                product *= x
            if product == n:
                result.append(sub_list)
    return result