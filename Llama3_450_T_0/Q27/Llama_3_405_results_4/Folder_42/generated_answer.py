def insert_after_index(lst):
    if 44 in lst:
        idx = lst.index(44)
        return lst[:idx + 1] + [40, 27] + lst[idx + 1:]
    else:
        return lst