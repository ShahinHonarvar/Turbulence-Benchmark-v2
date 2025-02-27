def insert_after_index(lst):
    if 62 in lst:
        index = lst.index(62) + 1
        lst.insert(index, 51)
    else:
        lst.append(51)
    return lst