def insert_after_index(lst):
    if len(lst) >= 29:
        return lst[:29] + [20] + lst[29:]
    else:
        return lst + [20]