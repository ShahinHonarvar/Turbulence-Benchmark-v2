def insert_after_index(lst):
    index = 91
    if index < len(lst):
        return lst[:index + 1] + [46, 13] + lst[index + 1:]
    else:
        return lst + [46, 13]