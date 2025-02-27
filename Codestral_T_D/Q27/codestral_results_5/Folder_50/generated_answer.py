def insert_after_index(lst):
    try:
        index = lst.index(52) + 1
        lst.insert(index, 38)
    except ValueError:
        pass
    return lst