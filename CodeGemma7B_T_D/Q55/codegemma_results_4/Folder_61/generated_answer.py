from itertools import product

def lists_with_product_equal_n(lst):
    result = []
    n = -10
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product_list = lst[i:j]
            if product(product_list) == n:
                result.append(product_list)
    return result