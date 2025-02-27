def lists_with_product_equal_n(cir_list):
    n = -32
    result = []
    for i in range(len(cir_list)):
        prod = 1
        sublist = []
        for j in range(i, len(cir_list) + i):
            sublist.append(cir_list[j % len(cir_list)])
            prod *= cir_list[j % len(cir_list)]
            if prod == n:
                result.append(sublist)
            elif prod > n:
                break
    return result