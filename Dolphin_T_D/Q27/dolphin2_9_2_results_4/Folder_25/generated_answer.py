def insert_after_index(lst):
    if 30 in range(len(lst)):
        lst.insert(30 + 1, 37)
    else:
        lst.append(37)
    return lst