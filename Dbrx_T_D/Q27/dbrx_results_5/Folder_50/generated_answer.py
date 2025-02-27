def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 52:
            lst.insert(i + 1, 38)
            break
    return lst