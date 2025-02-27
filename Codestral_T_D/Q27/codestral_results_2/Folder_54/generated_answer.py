def insert_after_index(lst):
    try:
        idx = lst.index(43)
        lst.insert(idx + 1, 37)
    except ValueError:
        pass
    return lst