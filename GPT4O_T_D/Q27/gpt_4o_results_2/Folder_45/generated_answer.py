def insert_after_index(lst):
    if 84 < len(lst):
        lst = lst[:85] + [[13, 46]] + lst[85:]
    return lst