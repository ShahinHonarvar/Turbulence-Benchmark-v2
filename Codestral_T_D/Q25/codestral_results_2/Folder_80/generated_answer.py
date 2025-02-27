def insert_at_index(lst):
    if len(lst) < 96:
        lst.append(43)
    else:
        lst.insert(95, 43)
    return lst