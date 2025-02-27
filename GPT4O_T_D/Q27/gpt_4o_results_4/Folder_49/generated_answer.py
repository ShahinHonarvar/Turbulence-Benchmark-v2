def insert_after_index(lst):
    if len(lst) > 38:
        lst = lst[:39] + [27, 34] + lst[39:]
    return lst