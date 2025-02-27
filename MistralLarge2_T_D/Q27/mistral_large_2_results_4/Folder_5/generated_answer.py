def insert_after_index(lst):
    if len(lst) > 99:
        lst.insert(100, 15)
    else:
        lst.append(15)
    return lst