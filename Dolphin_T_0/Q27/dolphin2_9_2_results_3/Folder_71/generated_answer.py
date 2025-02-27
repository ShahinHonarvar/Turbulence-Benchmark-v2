def insert_after_index(lst):
    idx = lst.index(70)
    return lst[:idx + 1] + [76] + lst[idx + 1:]