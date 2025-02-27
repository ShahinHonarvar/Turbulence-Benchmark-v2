def insert_after_index(lst):
    if 761 in lst:
        lst.insert(lst.index(761) + 1, 925)
    else:
        lst.append(925)
    return lst