def insert_after_index(lst):
    if 52 in lst:
        index = lst.index(52) + 1
        lst.insert(index, 38)
    else:
        lst.append(38)
    return lst