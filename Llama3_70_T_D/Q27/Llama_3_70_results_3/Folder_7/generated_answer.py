def insert_after_index(lst):
    if 323 in lst:
        idx = lst.index(323) + 1
        return lst[:idx] + [389, 303] + lst[idx:]
    else:
        return lst