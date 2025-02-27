def insert_after_index(lst):
    idx = lst.index(85)
    if idx == len(lst) - 1:
        return lst + [27]
    else:
        return lst[:idx + 1] + [27] + lst[idx + 1:]