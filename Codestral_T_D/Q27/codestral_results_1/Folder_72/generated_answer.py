def insert_after_index(lst):
    try:
        index = lst.index(24)
        lst.insert(index + 1, [98, 22])
    except ValueError:
        pass
    return lst