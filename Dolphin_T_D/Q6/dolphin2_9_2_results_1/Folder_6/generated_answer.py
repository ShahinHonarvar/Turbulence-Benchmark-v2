def all_neg_ints_exclusive(lst):
    if len(lst) < 99:
        return []
    return [x for x in lst[87:99] if x < 0]