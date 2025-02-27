def lists_with_product_equal_n(circular_list):
    n = -5
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j + 1]
            if j >= len(circular_list):
                sublist += circular_list[0:j - len(circular_list) + 1]
            product = 1
            for k in sublist:
                product *= k
            if product == n:
                result.append(sublist)
    return result