def all_neg_ints_exclusive(lst):
    if len(lst) < 46:
        return []
    return [i for i in lst[24:45] if i < 0]