def insert_at_index(lst):
    if len(lst) >= 74:
        lst.insert(74, 517.71)
    else:
        lst += [None] * (74 - len(lst)) + [517.71]
    return lst