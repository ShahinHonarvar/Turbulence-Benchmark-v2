def insert_after_index(lst):
    if len(lst) > 74:
        return lst[:75] + [49] + lst[75:]
    else:
        return lst + [49]