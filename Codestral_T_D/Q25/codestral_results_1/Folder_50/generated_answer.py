def insert_at_index(lst):
    if len(lst) > 52:
        lst.insert(52, 38)
    else:
        lst.append(38)
    return lst