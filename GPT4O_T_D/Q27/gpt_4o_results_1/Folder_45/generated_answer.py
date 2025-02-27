def insert_after_index(lst):
    if len(lst) > 84:
        lst = lst[:85] + [13, 46] + lst[85:]
    return lst