def insert_after_index(lst):
    try:
        i = lst.index(95) + 1
        return lst[:i] + [43] + lst[i:]
    except ValueError:
        return lst