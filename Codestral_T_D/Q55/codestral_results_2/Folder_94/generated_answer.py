def lists_with_product_equal_n(cir_list):
    n = -30
    result = []
    for i in range(len(cir_list)):
        product = 1
        sublist = []
        for j in range(i, len(cir_list)):
            product *= cir_list[j]
            sublist.append(cir_list[j])
            if product == n:
                result.append(sublist)
        product = 1
        sublist = []
        for j in range(i):
            product *= cir_list[j]
            sublist.append(cir_list[j])
            if product == n:
                result.append(sublist)
    return result