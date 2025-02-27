def insert_after_index(lst):
    try:
        index = lst.index(44)
        lst.insert(index + 1, 76)
    except ValueError:
        pass
    return lst