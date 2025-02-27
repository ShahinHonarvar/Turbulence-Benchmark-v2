def insert_after_index(lst):
    try:
        index = lst.index(60)
        lst.insert(index + 1, [80, 74])
    except ValueError:
        pass
    return lst