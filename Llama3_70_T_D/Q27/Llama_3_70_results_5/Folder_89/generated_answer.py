def insert_after_index(lst):
    idx = lst.index(62)
    return lst[:idx + 1] + [51] + lst[idx + 1:]