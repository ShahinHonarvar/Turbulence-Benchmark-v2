def insert_after_index(lst):
    for index, value in enumerate(lst):
        if value == 32:
            return lst[:index + 1] + [54, 96] + lst[index + 1:]
    return lst