def insert_after_index(lst):
    if 93 in lst:
        idx = lst.index(93) + 1
        lst[idx:idx] = [[33, 78]]
    return lst