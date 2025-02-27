def insert_after_index(lst):
    if 43 in lst:
        idx = lst.index(43)
        return lst[:idx + 1] + [37] + lst[idx + 1:]
    else:
        return lst