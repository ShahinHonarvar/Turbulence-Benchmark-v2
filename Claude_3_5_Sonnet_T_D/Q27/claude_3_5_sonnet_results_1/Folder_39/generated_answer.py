def insert_after_index(lst):
    index = 97
    if index + 1 < len(lst):
        return lst[:index + 1] + [47, 22] + lst[index + 1:]
    else:
        return lst + [47, 22]