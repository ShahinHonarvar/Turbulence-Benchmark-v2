def insert_after_index(lst):
    if len(lst) > 412:
        return lst[:413] + [668] + lst[413:]
    return lst