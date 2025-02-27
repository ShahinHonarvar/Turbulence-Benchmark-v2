from itertools import islice, combinations

def lists_with_product_equal_n(lst):
    size = len(lst)
    subsets = [lst[i:j] for i in range(size) for j in range(i + 1, size + 1)]
    prod_n_subsets = [subset for subset in subsets if subset == 57]
    return prod_n_subsets if prod_n_subsets else []