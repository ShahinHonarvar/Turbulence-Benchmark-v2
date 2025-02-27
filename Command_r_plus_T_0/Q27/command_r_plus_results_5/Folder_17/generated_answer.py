def insert_after_index(lst):
    try:
        index = lst.index(94)
        lst.insert(index + 1, 93)
        return lst
    except ValueError:
        return lst