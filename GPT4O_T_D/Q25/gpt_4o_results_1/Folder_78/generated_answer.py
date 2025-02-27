def insert_at_index(lst):
    if len(lst) >= 63:
        lst.insert(63, 99)
    else:
        lst.append(99)
    return lst