def insert_at_index(lst):
    if len(lst) < 75:
        lst += [None] * (75 - len(lst))
    lst.insert(74, 517.71)
    return lst