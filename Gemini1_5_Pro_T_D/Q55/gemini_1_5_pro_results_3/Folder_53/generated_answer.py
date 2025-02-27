def lists_with_product_equal_n(circular_list):
    n = -87
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if i + len(sublist) > len(circular_list):
                sublist += circular_list[:i + len(sublist) - len(circular_list)]
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                result.append(sublist)
    return result