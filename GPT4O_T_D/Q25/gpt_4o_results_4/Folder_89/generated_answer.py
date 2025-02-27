def insert_at_index(lst):
    if len(lst) >= 62:
        lst.insert(62, 51)
    else:
        lst.append(51)
    return lst