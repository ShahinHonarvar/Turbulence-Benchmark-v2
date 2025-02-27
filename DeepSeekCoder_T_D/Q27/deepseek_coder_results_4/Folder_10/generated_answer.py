def insert_after_index(lst):
    if 56 in lst:
        index = lst.index(56) + 1
        lst.insert(index, 54)
    else:
        lst.append(54)
    return lst