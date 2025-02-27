def insert_after_index(lst):
    try:
        index = lst.index(43)
        lst.insert(index + 1, 37)
    except ValueError:
        lst.append(37)
    return lst