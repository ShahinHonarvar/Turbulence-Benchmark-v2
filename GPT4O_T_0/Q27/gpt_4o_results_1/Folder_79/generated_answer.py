def insert_after_index(lst):
    if len(lst) > 28:
        return lst[:29] + [41, 69] + lst[29:]
    return lst