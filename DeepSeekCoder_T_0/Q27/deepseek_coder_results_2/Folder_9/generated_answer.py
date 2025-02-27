def insert_after_index(lst):
    if 66 in lst:
        lst.insert(lst.index(66) + 1, 45)
    else:
        lst.append(45)
    return lst