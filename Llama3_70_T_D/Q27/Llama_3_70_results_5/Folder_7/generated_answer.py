def insert_after_index(lst):
    return lst[:lst.index(323) + 1] + [389, 303] + lst[lst.index(323) + 1:]