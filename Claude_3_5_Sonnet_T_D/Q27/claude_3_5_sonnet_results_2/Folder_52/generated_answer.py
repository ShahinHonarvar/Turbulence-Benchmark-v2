def insert_after_index(lst):
    index = 97
    if index < len(lst):
        return lst[:index + 1] + [72.27] + lst[index + 1:]
    else:
        return lst + [72.27]