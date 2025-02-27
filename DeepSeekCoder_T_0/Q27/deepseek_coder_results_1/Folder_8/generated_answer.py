def insert_after_index(lst):
    if 57 in lst:
        lst.insert(lst.index(57) + 1, 76)
    else:
        lst.append(76)
    return lst