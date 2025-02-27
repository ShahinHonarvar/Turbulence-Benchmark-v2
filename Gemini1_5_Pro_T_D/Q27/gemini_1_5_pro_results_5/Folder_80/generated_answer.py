def insert_after_index(lst):
    try:
        i = lst.index(95)
        return lst[:i + 1] + [43] + lst[i + 1:]
    except:
        return lst