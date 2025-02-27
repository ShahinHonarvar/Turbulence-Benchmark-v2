def insert_after_index(lst):
    try:
        index = lst.index(31)
        lst.insert(index + 1, [88, 51])
    except ValueError:
        pass
    return lst