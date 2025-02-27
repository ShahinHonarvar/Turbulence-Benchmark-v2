def insert_after_index(lst):
    if len(lst) > 38:
        return lst[:39] + [27, 34] + lst[39:]
    return lst