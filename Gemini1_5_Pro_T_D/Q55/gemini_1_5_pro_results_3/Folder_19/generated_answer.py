def lists_with_product_equal_n(circular_list):
    n = -54
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if j + 1 >= len(circular_list) and i != 0:
                sublist += circular_list[:i]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    return result