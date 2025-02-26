def insert_after_index(lst):
    try:
        index = lst.index(85)
        lst.insert(index + 1, 27)
    except ValueError:
        pass
    return lst