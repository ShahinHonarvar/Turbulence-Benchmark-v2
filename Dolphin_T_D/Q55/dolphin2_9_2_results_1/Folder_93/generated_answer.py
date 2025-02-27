def lists_with_product_equal_n(input_list):
    product_equal_n_lists = []
    n = len(input_list)
    for i in range(n):
        for size in range(2, n + 1):
            if i + size <= n:
                product = 1
                for j in range(i, i + size):
                    product *= input_list[j % n]
                if product == -91:
                    product_equal_n_lists.append(input_list[i:i + size])
    return product_equal_n_lists