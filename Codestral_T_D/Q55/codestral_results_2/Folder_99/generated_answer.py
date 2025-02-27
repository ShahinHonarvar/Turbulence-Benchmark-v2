def lists_with_product_equal_n(cir_list):
    n = 415
    result = []
    for i in range(len(cir_list)):
        product = 1
        sublist = []
        for j in range(i, len(cir_list) + i):
            product *= cir_list[j % len(cir_list)]
            sublist.append(cir_list[j % len(cir_list)])
            if product == n:
                result.append(sublist)
            if product > n:
                break
    return result