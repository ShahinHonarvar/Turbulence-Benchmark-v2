def insert_at_index(lst):
    if len(lst) < 100:
        lst.append(15)
    else:
        lst.insert(99, 15)
    return lst