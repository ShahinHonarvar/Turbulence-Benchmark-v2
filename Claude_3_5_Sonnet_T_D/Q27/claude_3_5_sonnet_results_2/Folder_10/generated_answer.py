def insert_after_index(lst):
    try:
        index = lst.index(56)
        lst.insert(index + 1, 54)
    except ValueError:
        pass
    return lst