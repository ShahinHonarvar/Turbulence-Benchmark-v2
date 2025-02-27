def insert_after_index(lst):
    for i, element in enumerate(lst):
        if element == 63:
            lst.insert(i + 1, 99)
    return lst