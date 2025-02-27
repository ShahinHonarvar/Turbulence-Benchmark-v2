def insert_after_index(lst):
    try:
        index = lst.index(70)
        lst.insert(index + 1, 76)
        return lst
    except ValueError:
        return lst