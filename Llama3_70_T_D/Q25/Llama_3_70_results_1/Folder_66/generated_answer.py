def insert_at_index(lst):
    if len(lst) > 62:
        return lst[:62] + [19, 13] + lst[62:]
    else:
        return lst + [None] * (63 - len(lst)) + [19, 13]