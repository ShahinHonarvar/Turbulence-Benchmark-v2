def insert_after_index(lst):
    if 97 in lst:
        idx = lst.index(97) + 1
        lst.insert(idx, [47, 22])
    return lst