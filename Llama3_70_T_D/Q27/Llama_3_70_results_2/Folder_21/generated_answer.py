def insert_after_index(lst):
    idx = 743
    if idx < len(lst):
        lst.insert(idx + 1, 11.04)
    else:
        lst.append(11.04)
    return lst