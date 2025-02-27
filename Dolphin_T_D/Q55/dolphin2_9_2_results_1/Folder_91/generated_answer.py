def lists_with_product_equal_n(num_list):
    product_list = []
    n = len(num_list)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= num_list[j % n]
            if product == 2:
                product_list.append(num_list[i:j + 1])
                break
    return product_list