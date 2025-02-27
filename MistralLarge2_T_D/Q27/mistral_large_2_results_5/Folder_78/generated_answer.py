def insert_after_index(lst):
    if len(lst) > 63:
        lst.insert(64, 99)
    else:
        lst.append(99)
    return lst