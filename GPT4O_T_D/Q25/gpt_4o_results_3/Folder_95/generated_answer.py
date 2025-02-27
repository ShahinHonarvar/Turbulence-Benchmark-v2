def insert_at_index(lst):
    if len(lst) >= 20:
        lst.insert(20, 80)
    else:
        lst.append(80)
    return lst