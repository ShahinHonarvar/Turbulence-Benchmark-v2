def insert_after_index(lst):
    for i, item in enumerate(lst):
        if i == 96:
            lst.insert(i + 1, 36)
            break
    return lst