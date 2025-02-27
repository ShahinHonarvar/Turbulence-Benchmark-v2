def insert_after_index(lst):
    if len(lst) > 9:
        lst.insert(10, 1)
    else:
        lst.append(1)
    return lst