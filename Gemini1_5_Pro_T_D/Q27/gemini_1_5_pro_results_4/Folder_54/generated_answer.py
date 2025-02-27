def insert_after_index(lst):
    idx = lst.index(43)
    return lst[:idx + 1] + [37] + lst[idx + 1:]