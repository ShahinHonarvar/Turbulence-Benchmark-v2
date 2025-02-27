def insert_after_index(lst):
    try:
        index = lst.index(52)
        return lst[:index + 1] + [38] + lst[index + 1:]
    except ValueError:
        return lst + [38]