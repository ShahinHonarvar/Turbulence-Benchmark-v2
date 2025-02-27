def insert_after_index(lst):
    for i, value in enumerate(lst):
        if value == 99:
            lst.insert(i + 1, 99)
            break
    return lst