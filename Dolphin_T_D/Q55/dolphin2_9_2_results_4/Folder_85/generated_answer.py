def lists_with_product_equal_n(input_list):
    result = []
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list) + 1):
            product = 1
            sublist = input_list[i:j]
            if j - i == len(input_list):
                sublist = sublist + input_list[:i]
            for k in sublist:
                product *= k
            if product == -97:
                result.append(sublist)
    return result