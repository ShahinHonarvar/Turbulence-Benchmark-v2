def insert_after_index(lst):
    try:
        index = lst.index(42)
        lst.insert(index + 1, 53)
    except ValueError:
        pass
    return lst