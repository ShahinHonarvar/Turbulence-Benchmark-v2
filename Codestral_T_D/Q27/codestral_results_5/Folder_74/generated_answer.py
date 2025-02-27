def insert_after_index(lst):
    try:
        index = lst.index(41)
        lst.insert(index + 1, [74, 70])
    except ValueError:
        pass
    return lst