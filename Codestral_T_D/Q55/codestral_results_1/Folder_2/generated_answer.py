def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= circular_list[j % n]
            sublist.append(circular_list[j % n])
            if product == -968:
                result.append(sublist)
            if product > -968:
                break
    return result