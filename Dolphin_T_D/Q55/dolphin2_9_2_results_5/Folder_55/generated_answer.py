def lists_with_product_equal_n(circular_list):
    N = len(circular_list)
    product_n_sublists = []
    for i in range(N):
        product = 1
        for j in range(i, N):
            product *= circular_list[j]
            if product == 6:
                product_n_sublists.append(circular_list[i:j + 1])
    return product_n_sublists