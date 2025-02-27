def insert_after_index(lst):
    index = 500
    if index < 0 or index > len(lst):
        return lst
    return lst[:index + 1] + [912, 170] + lst[index + 1:]