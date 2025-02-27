def insert_after_index(lst):
    if len(lst) > 9:
        lst.insert(lst.index(9) + 1, 1)
    else:
        lst.append(1)
    return lst