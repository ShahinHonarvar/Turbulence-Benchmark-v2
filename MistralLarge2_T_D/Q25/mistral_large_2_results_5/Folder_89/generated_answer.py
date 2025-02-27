def insert_at_index(lst):
    if len(lst) < 62:
        lst.extend([None] * (62 - len(lst)))
    lst.insert(62, 51)
    return lst