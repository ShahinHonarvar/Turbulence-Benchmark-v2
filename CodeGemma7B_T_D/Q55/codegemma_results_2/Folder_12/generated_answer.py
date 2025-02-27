from itertools import product

def lists_with_product_equal_n(circular_list):
    for sublist_size in range(1, len(circular_list) + 1):
        for sublist in product(circular_list, repeat=sublist_size):
            if prod(sublist) == -18:
                return list(sublist)
    return []