def insert_after_index(lst):
    try:
        index = lst.index(38)
        return lst[:index + 1] + [27, 34] + lst[index + 1:]
    except ValueError:
        return lst