def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 94:
            lst.insert(i + 1, 93)
            break
    return lst