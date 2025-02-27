def insert_after_index(lst):
    if len(lst) > 42:
        lst.insert(43, 53)
    else:
        lst.append(53)
    return lst