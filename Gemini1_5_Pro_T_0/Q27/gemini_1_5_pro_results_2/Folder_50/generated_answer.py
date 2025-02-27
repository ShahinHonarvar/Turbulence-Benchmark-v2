def insert_after_index(lst):
    try:
        i = lst.index(52)
        return lst[:i + 1] + [38] + lst[i + 1:]
    except ValueError:
        return lst