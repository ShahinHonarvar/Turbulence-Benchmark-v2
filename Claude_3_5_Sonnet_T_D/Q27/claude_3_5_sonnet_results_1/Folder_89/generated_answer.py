def insert_after_index(lst):
    try:
        index = lst.index(62)
        lst.insert(index + 1, 51)
    except ValueError:
        pass
    return lst