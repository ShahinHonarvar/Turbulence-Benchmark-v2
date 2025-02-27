def insert_after_index(lst):
    if 99 < len(lst):
        lst.insert(100, 15)
    else:
        lst.append(15)
    return lst