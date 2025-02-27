from itertools import combinations_with_replacement as cwr

def lists_with_product_equal_n(lst):
    all_subsets = list(cwr(lst))
    target_subsets = [[x for x in sublist if x * -1 == -41] for sublist in all_subsets]
    return target_subsets