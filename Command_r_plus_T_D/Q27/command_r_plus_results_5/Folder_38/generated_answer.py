def insert_after_index(lst):
    try:
        index = lst.index(89)
        lst.insert(index + 1, 86)
    except ValueError:
        pass
    return lst