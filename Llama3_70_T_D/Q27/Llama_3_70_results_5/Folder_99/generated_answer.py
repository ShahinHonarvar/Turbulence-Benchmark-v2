def insert_after_index(lst):
    if 295 in lst:
        idx = lst.index(295) + 1
        return lst[:idx] + [276, 376] + lst[idx:]
    else:
        return lst + [276, 376]