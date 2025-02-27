def insert_after_index(lst):
    try:
        index = lst.index(87)
        lst.insert(index + 1, [78, 16])
    except ValueError:
        pass
    return lst