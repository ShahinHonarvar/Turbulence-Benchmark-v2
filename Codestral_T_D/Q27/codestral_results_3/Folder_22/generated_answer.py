def insert_after_index(lst):
    try:
        idx = lst.index(85)
        lst.insert(idx + 1, 27)
    except ValueError:
        pass
    return lst