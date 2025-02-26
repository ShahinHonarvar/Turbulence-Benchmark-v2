def insert_after_index(lst):
    try:
        index = lst.index(69)
        lst.insert(index + 1, 92)
    except ValueError:
        pass
    return lst