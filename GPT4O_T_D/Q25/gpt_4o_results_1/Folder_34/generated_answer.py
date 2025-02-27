def insert_at_index(lst):
    if len(lst) < 53:
        lst.extend([None] * (53 - len(lst) + 1))
    lst.insert(53, 783.25)
    return lst