def insert_after_index(lst):
    try:
        index = lst.index(66)
        lst.insert(index + 1, 45)
    except ValueError:
        pass
    return lst