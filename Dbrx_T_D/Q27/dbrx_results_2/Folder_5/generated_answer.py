def insert_after_index(lst):
    for i, v in enumerate(lst):
        if v == 99:
            lst.insert(i + 1, 15)
            break
    return lst