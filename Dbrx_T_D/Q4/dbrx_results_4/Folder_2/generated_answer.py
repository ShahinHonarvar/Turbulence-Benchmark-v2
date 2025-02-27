def all_pos_ints_exclusive(lst):
    if len(lst) < 53 or not lst[36:52]:
        return []
    else:
        return [i for i in lst[36:52] if i > 0]