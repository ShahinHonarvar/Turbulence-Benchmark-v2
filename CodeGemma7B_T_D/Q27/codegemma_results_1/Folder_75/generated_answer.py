def insert_after_index(lst):
    for i, x in enumerate(lst):
        if x == 99:
            lst.insert(i + 1, 99)
    return lst