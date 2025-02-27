def insert_after_index(lst):
    if 56 in lst:
        lst.insert(lst.index(56) + 1, 54)
    else:
        lst.append(54)
    return lst