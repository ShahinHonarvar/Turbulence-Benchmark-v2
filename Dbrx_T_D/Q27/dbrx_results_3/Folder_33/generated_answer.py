def insert_after_index(lst):
    index = 556
    value = 974.0
    if index >= 0 and index < len(lst):
        return lst[:index + 1] + [value] + lst[index + 1:]
    else:
        return lst