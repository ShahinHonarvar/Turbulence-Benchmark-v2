def insert_after_index(lst):
    try:
        idx = lst.index(31) + 1
        lst[idx:idx] = [[88, 51]]
    except ValueError:
        pass
    return lst