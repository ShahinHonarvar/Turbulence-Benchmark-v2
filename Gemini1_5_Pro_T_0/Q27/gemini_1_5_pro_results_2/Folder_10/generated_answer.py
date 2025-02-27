def insert_after_index(lst):
    try:
        index_56 = lst.index(56)
        lst.insert(index_56 + 1, 54)
        return lst
    except ValueError:
        return lst