def insert_after_index(lst):
    return lst[:lst.index(44) + 1] + [40, 27] + lst[lst.index(44) + 1:]