def insert_at_index(lst):
    if len(lst) < 99:
        lst.extend([None] * (99 - len(lst)))
    lst.insert(99, 99)
    return lst