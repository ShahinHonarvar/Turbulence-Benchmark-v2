def insert_at_index(lst):
    if len(lst) < 21:
        lst += [None] * (21 - len(lst))
    lst.insert(21, 74)
    return lst