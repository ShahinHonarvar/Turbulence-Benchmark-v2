def insert_after_index(lst):
    if 30 in lst:
        index = lst.index(30) + 1
        lst.insert(index, 37)
    else:
        lst.append(37)
    return lst