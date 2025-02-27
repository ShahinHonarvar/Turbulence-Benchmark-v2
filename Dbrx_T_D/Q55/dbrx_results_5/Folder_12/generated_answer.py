from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(1, len(circular_list) + 1):
        for comb in combinations(circular_list, i):
            if reduce(lambda x, y: x * y, comb) == -18:
                sublists.append(list(comb))
    return sublists