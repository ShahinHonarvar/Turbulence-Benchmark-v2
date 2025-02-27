def insert_after_index(lst):
    try:
        index = lst.index(21)
        lst.insert(index + 1, 74)
    except ValueError:
        pass
    return lst