def insert_after_index(lst):
    if len(lst) > 29:
        return lst[:30] + [28, 53] + lst[30:]
    return lst