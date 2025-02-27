def insert_after_index(lst):
    if len(lst) > 95:
        return lst[:96] + [43] + lst[96:]
    return lst