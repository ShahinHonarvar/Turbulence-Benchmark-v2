def insert_after_index(lst):
    try:
        i = lst.index(70) + 1
        lst = lst[:i] + [76] + lst[i:]
    except ValueError:
        pass
    return lst