def insert_after_index(lst):
    if 500 < len(lst) - 1:
        lst.insert(501, [912, 170])
    else:
        lst.append([912, 170])
    return lst