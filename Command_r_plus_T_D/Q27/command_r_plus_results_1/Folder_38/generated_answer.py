def insert_after_index(lst):
    try:
        index = lst.index(89)
        lst.insert(index + 1, 86)
        return lst
    except ValueError:
        return lst