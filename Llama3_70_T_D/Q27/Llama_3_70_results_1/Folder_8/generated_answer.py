def insert_after_index(lst):
    index = 57
    if index < len(lst):
        return lst[:index + 1] + [76] + lst[index + 1:]
    else:
        return lst + [76]