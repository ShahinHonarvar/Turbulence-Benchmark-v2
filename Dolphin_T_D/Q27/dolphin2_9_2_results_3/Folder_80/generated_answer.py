def insert_after_index(lst):
    try:
        index95 = lst.index(95)
        return lst[:index95 + 1] + [43] + lst[index95 + 1:]
    except ValueError:
        return lst + [43]