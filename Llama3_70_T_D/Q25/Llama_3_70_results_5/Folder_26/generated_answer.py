def insert_at_index(lst):
    if len(lst) < 55:
        lst.extend([None] * (55 - len(lst)))
    lst.insert(55, [26, 10])
    return lst