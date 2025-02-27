def insert_after_index(lst):
    for i, element in enumerate(lst):
        if i == 166:
            lst.insert(i + 1, 232)
    return lst