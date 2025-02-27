def insert_after_index(lst):
    if 66 in lst:
        index = lst.index(66) + 1
        lst.insert(index, 45)
    else:
        lst.append(45)
    return lst