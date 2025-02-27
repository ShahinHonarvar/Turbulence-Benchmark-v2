from itertools import combinations_with_replacement

def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] * lst[j] == 49:
                sublists.append([lst[i], lst[j]])
    return sublists