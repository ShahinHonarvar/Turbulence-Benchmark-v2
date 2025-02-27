def insert_after_index(lst):
    try:
        index = lst.index(56)
        return lst[:index + 1] + [54] + lst[index + 1:]
    except ValueError:
        return lst