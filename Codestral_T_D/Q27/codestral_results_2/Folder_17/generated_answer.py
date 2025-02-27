def insert_after_index(lst):
    try:
        idx = lst.index(94)
        lst.insert(idx + 1, 93)
    except ValueError:
        pass
    return lst