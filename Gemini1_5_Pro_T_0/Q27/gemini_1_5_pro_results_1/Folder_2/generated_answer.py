def insert_after_index(lst):
    idx = lst.index(427) + 1
    return lst[:idx] + [312, 441] + lst[idx:]