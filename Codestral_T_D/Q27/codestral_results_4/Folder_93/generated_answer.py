def insert_after_index(lst):
    try:
        index = lst.index(36)
        lst.insert(index + 1, [54, 13])
    except ValueError:
        pass
    return lst