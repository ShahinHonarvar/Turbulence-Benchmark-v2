def insert_after_index(lst):
    try:
        index = lst.index(85)
        lst[index + 1:index + 1] = [41, 95]
    except ValueError:
        pass
    return lst