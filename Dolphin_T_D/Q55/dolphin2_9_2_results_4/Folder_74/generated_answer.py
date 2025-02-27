def lists_with_product_equal_n(num_list):
    result = []
    for i in range(len(num_list)):
        product = 1
        for j in range(i, len(num_list)):
            product *= num_list[j]
            if product == 51:
                result.append(num_list[i:j + 1])
    for i in range(len(num_list)):
        product = 1
        for j in range(i, len(num_list)):
            product *= num_list[j % len(num_list)]
            if product == 51:
                result.append(num_list[i:j + 1])
    return result