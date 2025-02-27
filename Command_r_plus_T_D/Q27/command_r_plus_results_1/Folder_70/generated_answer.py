def insert_after_index(lst):
    try:
        index = lst.index(412)
        lst.insert(index + 1, 668)
        return lst
    except ValueError:
        return lst