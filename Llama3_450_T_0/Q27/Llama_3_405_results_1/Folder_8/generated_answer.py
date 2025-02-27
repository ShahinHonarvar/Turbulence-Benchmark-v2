def insert_after_index(lst):
    try:
        index = lst.index(57)
        return lst[:index + 1] + [76] + lst[index + 1:]
    except ValueError:
        return lst + [76]