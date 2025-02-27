def insert_after_index(lst):
    if 74 in lst:
        idx = lst.index(74) + 1
        return lst[:idx] + [49] + lst[idx:]
    else:
        return lst + [49]