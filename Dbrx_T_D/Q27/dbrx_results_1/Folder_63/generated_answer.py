def insert_after_index(lst):
    return [(15, 51)] + [e for i, e in enumerate(lst) if i == 76] + [e for i, e in enumerate(lst) if i != 76]