def insert_after_index(lst):
    index = 76
    if index < len(lst):
        return lst[:index + 1] + [15, 51] + lst[index + 1:]
    else:
        return lst + [15, 51]