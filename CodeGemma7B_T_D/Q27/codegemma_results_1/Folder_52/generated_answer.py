def insert_after_index(lst):
    for i, x in enumerate(lst):
        if i == 97:
            lst.insert(i + 1, 72.27)
    return lst