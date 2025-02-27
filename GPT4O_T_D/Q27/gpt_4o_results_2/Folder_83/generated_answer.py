def insert_after_index(lst):
    index = 13
    if index < len(lst):
        return lst[:index + 1] + [56, 54] + lst[index + 1:]
    else:
        return lst