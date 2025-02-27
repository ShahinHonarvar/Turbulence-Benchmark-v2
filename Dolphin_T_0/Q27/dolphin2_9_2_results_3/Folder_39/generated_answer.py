def insert_after_index(lst):
    if len(lst) <= 97:
        return lst + [47, 22]
    else:
        return lst[:98] + [47, 22] + lst[98:]