def insert_after_index(lst):
    if len(lst) > 40:
        return lst[:41] + [169.26] + lst[41:]
    return lst + [169.26]