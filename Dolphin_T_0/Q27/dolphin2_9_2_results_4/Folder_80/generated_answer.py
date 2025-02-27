def insert_after_index(lst):
    if 95 in lst:
        index = lst.index(95)
        lst.insert(index + 1, 43)
    else:
        lst.append(43)
    return lst