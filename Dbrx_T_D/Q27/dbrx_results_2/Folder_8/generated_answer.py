def insert_after_index(lst):
    for index, value in enumerate(lst):
        if index == 57:
            return lst[:index + 1] + [76] + lst[index + 1:]
    return lst + [76]