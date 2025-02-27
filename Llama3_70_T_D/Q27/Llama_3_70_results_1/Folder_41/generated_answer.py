def insert_after_index(lst):
    try:
        index = lst.index(87)
        return lst[:index + 1] + [78, 16] + lst[index + 1:]
    except ValueError:
        return lst