def insert_after_index(lst):
    try:
        index = lst.index(983)
        return lst[:index + 1] + [369] + lst[index + 1:]
    except ValueError:
        return lst + [983, 369]