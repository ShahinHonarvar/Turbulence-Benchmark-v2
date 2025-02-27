def insert_after_index(lst):
    return lst[:lst.index(85) + 1] + [41, 95] + lst[lst.index(85) + 1:]