def insert_after_index(lst):
    try:
        i = lst.index(70)
        return lst[:i + 1] + [76] + lst[i + 1:]
    except:
        return lst