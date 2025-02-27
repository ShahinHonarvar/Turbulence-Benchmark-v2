def insert_after_index(lst):
    try:
        index = lst.index(89) + 1
        lst = lst[:index] + [86] + lst[index:]
        return lst
    except ValueError:
        return lst