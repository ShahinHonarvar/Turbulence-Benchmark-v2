def lists_with_product_equal_n(circular_list):
    n = 247
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if j == len(circular_list) and i != 0:
                sublist += circular_list[:i]
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                result.append(sublist)
    return result