def insert_after_index(lst):
    idx = lst.index(761)
    return lst[:idx + 1] + [925] + lst[idx + 1:]