def insert_after_index(lst):
    try:
        index = lst.index(90)
        lst.insert(index + 1, 80)
    except ValueError:
        pass
    return lst