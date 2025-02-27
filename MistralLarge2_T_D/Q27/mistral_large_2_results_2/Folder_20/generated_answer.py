def insert_after_index(lst):
    if len(lst) > 32:
        lst.insert(33, [54, 96])
    else:
        lst.extend([None] * (33 - len(lst)) + [[54, 96]])
    return lst