def lists_with_product_equal_n(num_list):
    result = []
    product_n = -968
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list) + 1):
            sublist = num_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == product_n:
                result.append(sublist)
    return result