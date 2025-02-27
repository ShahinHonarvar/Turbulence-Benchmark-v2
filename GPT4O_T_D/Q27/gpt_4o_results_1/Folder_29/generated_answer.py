def insert_after_index(lst):
    if len(lst) > 96:
        return lst[:97] + [36] + lst[97:]
    return lst