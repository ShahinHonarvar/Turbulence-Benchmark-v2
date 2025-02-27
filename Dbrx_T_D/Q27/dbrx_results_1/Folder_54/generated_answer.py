def insert_after_index(lst):
    index = 43
    if index < len(lst) - 1:
        return lst[:index + 1] + [37] + lst[index + 1:]
    else:
        return lst + [37]