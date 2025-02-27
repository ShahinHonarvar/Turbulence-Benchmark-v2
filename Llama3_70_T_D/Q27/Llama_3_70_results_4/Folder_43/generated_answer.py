def insert_after_index(lst):
    if len(lst) > 29:
        return lst[:29] + [28, 53] + lst[29:]
    else:
        return lst