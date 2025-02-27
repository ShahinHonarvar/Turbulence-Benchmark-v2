def insert_after_index(lst):
    if len(lst) > 62:
        return lst[:63] + [19, 13] + lst[63:]
    else:
        return lst + [19, 13]