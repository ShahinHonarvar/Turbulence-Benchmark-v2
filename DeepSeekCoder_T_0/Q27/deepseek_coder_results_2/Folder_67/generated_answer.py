def insert_after_index(lst):
    if 44 in lst:
        index = lst.index(44) + 1
        lst.insert(index, 76)
    else:
        lst.append(76)
    return lst