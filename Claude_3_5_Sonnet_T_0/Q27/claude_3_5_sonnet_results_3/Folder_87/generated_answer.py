def insert_after_index(lst):
    index = 69
    if index < len(lst):
        return lst[:index + 1] + [92] + lst[index + 1:]
    else:
        return lst + [92]