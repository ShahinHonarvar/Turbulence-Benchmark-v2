def insert_after_index(lst):
    if len(lst) > 70:
        lst.insert(71, 76)
    else:
        lst.append(76)
    return lst