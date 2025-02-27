def insert_after_index(lst):
    try:
        index = lst.index(100) + 1
        lst.insert(index, [876, 203])
    except ValueError:
        pass
    return lst