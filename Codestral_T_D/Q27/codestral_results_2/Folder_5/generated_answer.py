def insert_after_index(lst):
    try:
        index = lst.index(99)
        lst.insert(index + 1, 15)
    except ValueError:
        lst.append(15)
    return lst