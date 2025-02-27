from itertools import combinations_with_replacement

def lists_with_product_equal_n(circular_list):
    for size in range(1, len(circular_list) + 1):
        for sublist in combinations_with_replacement(circular_list, size):
            if product_of_sublist(sublist) == -17:
                return sublist
    return []