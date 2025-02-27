def all_neg_ints_inclusive(lst):
    if len(lst) <= 87:
        return []
    return [i for i in lst[30:88] if i < 0]