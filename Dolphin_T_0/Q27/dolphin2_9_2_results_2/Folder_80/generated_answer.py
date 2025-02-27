def insert_after_index(lst):
    try:
        index = lst.index(95)
        lst.insert(index + 1, 43)
    except ValueError:
        pass
    return lst