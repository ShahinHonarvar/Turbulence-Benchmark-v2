from itertools import product

def lists_with_product_equal_n(circular_list):
    product_list = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            product_list.append(sublist)
    return product_list