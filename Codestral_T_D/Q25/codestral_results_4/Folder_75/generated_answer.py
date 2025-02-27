def insert_at_index(lst):
    if len(lst) < 100:
        lst.append(99)
    else:
        lst.insert(99, 99)
    return lst