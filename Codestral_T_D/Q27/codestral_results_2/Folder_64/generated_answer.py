def insert_after_index(lst):
    try:
        idx = lst.index(8)
        lst.insert(idx + 1, [3, 8])
        return lst
    except ValueError:
        return lst