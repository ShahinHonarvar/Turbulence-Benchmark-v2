def lists_with_product_equal_n(num_list):
    results = []
    list_length = len(num_list)
    for i in range(list_length):
        product = num_list[i]
        for j in range(i + 1, list_length):
            product *= num_list[j]
            if j == i + list_length - 1:
                j = -1
            if product == -30:
                temp_list = num_list[i:j + 1]
                results.append(temp_list)
    return results