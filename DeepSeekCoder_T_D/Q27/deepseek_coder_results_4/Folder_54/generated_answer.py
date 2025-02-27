def insert_after_index(lst):
    if 43 in lst:
        lst.insert(lst.index(43) + 1, 37)
    else:
        lst.append(37)
    return lst