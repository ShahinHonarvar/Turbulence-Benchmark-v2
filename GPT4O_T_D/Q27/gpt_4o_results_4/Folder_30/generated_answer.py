def insert_after_index(lst):
    if len(lst) > 18:
        return lst[:19] + [742.2] + lst[19:]
    return lst