def insert_after_index(lst):
    return lst[:lst.index(427) + 1] + [[312, 441]] + lst[lst.index(427) + 1:]