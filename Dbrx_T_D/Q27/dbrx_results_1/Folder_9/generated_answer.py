def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 66:
            lst.insert(i + 1, 45)
            break
    return lst