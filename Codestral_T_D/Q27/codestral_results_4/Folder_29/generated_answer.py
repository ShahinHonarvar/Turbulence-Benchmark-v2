def insert_after_index(lst):
    try:
        index = lst.index(96)
        lst.insert(index + 1, 36)
        return lst
    except ValueError:
        return lst