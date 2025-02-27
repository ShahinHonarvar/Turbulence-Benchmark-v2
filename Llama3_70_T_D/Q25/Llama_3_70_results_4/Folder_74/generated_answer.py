def insert_at_index(lst):
    if len(lst) < 41:
        return lst + [74, 70]
    else:
        return lst[:41] + [74, 70] + lst[41:]