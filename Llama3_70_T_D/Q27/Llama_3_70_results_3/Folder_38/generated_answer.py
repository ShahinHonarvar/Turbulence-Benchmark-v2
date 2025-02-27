def insert_after_index(lst):
    return lst[:lst.index(89) + 1] + [86] + lst[lst.index(89) + 1:]