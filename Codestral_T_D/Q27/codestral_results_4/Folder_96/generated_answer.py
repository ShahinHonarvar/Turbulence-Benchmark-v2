def insert_after_index(lst):
    try:
        index = lst.index(74)
        lst.insert(index + 1, [51, 29])
    except ValueError:
        pass
    return lst