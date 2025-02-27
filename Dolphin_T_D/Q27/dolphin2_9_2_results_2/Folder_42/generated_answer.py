def insert_after_index(lst):
    i = lst.index(44)
    return lst[:i + 1] + [40, 27] + lst[i + 1:]