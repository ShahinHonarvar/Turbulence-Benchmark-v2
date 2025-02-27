from itertools import product

def lists_with_product_equal_n(circular_list):
    product_equal_n_lists = []
    for i, j in product(circular_list, repeat=2):
        product_equal_n_lists.append([i, j])
    for i, j, k in product(circular_list, repeat=3):
        product_equal_n_lists.append([i, j, k])
    for i, j, k, l in product(circular_list, repeat=4):
        product_equal_n_lists.append([i, j, k, l])
    return product_equal_n_lists