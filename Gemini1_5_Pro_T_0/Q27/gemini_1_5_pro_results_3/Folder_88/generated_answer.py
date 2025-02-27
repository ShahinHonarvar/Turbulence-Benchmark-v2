def insert_after_index(lst):
    return lst[:lst.index(91) + 1] + [46, 13] + lst[lst.index(91) + 1:]