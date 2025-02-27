def insert_after_index(lst):
    for i, item in enumerate(lst):
        if item == 44:
            lst.insert(i + 1, [40, 27])
            return lst
    return lst