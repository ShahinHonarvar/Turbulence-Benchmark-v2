def insert_after_index(lst):
    try:
        index = lst.index(323)
        lst.insert(index + 1, 389)
        lst.insert(index + 2, 303)
    except ValueError:
        pass
    return lst