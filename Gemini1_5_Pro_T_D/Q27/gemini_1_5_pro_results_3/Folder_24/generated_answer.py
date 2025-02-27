def insert_after_index(lst):
    return lst[:lst.index(42) + 1] + [53] + lst[lst.index(42) + 1:]