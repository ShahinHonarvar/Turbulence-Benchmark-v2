def insert_after_index(lst):
    try:
        index = lst.index(43)
        lst.insert(index + 1, 37)
    except ValueError:
        pass
    return lst