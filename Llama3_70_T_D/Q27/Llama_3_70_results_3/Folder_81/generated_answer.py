def insert_after_index(lst):
    if len(lst) > 28 and lst[28] == 20:
        return lst[:29] + [20] + lst[29:]
    else:
        return lst