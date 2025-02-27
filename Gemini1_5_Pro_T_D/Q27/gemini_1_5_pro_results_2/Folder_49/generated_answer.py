def insert_after_index(lst):
    return lst[:lst.index(38) + 1] + [27, 34] + lst[lst.index(38) + 1:]