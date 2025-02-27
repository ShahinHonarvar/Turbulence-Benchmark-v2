from itertools import combinations

def lists_with_product_equal_n(circular_list, n=45):
    sublists = []
    for i in range(1, len(circular_list) + 1):
        for comb in combinations(circular_list, i):
            if n in comb and list(comb)[::-1] == list(comb):
                sublists.append(list(comb))
    return sublists