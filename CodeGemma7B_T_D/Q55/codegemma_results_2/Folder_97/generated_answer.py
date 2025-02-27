def lists_with_product_equal_n(cyclic_list):
    product = -938
    lists_of_product = []
    for i in range(len(cyclic_list)):
        current_product = cyclic_list[i]
        for j in range(i + 1, len(cyclic_list)):
            current_product *= cyclic_list[j]
            if current_product == product:
                list_of_product = cyclic_list[i:j + 1]
                lists_of_product.append(list_of_product)
                current_product = cyclic_list[j] * current_product
    return lists_of_product