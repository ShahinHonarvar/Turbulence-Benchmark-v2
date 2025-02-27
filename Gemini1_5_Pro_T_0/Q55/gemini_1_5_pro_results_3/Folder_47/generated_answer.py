def lists_with_product_equal_n(circular_list):
    n = -94
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if j == len(circular_list) - 1 and i != 0:
                sublist += circular_list[0:i]
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                result.append(sublist)
    return result