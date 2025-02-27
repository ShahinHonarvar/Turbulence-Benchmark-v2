def insert_after_index(lst):
    try:
        index = lst.index(20)
    except ValueError:
        return lst
    return lst[:index + 1] + [80] + lst[index + 1:]