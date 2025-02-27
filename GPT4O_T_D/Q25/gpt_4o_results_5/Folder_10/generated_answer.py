def insert_at_index(lst):
    if len(lst) < 56:
        lst.extend([None] * (56 - len(lst)))
    lst.insert(56, 54)
    return lst