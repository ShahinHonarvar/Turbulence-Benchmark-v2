def insert_after_index(lst):
    idx = lst.index(28)
    return lst[:idx + 1] + [20] + lst[idx + 1:]