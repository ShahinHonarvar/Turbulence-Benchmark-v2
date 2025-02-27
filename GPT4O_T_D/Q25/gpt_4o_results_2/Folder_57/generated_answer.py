def insert_at_index(lst):
    if len(lst) <= 90:
        lst.extend([None] * (91 - len(lst)))
    lst.insert(90, 80)
    return lst