def insert_after_index(lst):
    return lst[:lst.index(60) + 1] + [80, 74] + lst[lst.index(60) + 1:]