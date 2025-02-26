def insert_after_index(lst):
    try:
        index = lst.index(52)
        lst.insert(index + 1, 38)
    except ValueError:
        pass
    return lst