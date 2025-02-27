def insert_after_index(lst):
    if len(lst) > 62:
        lst = lst[:63] + [19, 13] + lst[63:]
    return lst