def insert_after_index(lst):
    if 427 in lst:
        idx = lst.index(427) + 1
        return lst[:idx] + [312, 441] + lst[idx:]
    else:
        return lst