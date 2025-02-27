from itertools import product

def lists_with_product_equal_n(lst):
    lst_len = len(lst)
    triple_lst = lst + lst[:2]
    sublist_start_end = [(i, i + 2) for i in range(lst_len)]
    sublists_equal_n = []
    for start, end in sublist_start_end:
        sublist = triple_lst[start:end + 1]
        if sublist != sorted(sublist, reverse=True):
            sublist_set = set(sublist)
            sublist_product = sublist[0] * sublist[1] * sublist[2]
            if sublist_product == -779 and len(sublist_set) != len(sublist):
                sublists_equal_n.append(sublist)
    return sublists_equal_n