def insert_after_index(lst):
    try:
        index = lst.index(89)
        return lst[:index + 1] + [86] + lst[index + 1:]
    except ValueError:
        return lst + [86]