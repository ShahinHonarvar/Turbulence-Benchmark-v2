def insert_after_index(lst):
    try:
        i = lst.index(983)
        return lst[:i + 1] + [369] + lst[i + 1:]
    except ValueError:
        return lst