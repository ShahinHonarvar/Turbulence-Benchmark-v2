def insert_after_index(lst):
    return lst[:lst.index(28) + 1] + [41, 69] + lst[lst.index(28) + 1:]