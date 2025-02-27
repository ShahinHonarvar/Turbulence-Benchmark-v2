def lists_with_product_equal_n(num_list):
    result = []
    for i in range(len(num_list)):
        sublist = []
        product = 1
        for j in range(i, len(num_list)):
            sublist.append(num_list[j])
            product *= num_list[j]
            if product == -938:
                result.append(sublist[:])
            elif product > -938:
                break
    return result