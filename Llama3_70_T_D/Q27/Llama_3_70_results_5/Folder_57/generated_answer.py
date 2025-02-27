def insert_after_index(lst):
    return lst[:lst.index(90) + 1] + [80] + lst[lst.index(90) + 1:]