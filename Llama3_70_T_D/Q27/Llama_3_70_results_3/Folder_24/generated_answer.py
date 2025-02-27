def insert_after_index(lst):
    index = 42
    if index < len(lst):
        return lst[:index + 1] + [53] + lst[index + 1:]
    else:
        return lst + [53]