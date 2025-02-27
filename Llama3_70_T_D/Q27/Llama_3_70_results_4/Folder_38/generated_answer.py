def insert_after_index(lst):
    index = len(lst) - 1 - lst[::-1].index(89)
    return lst[:index + 1] + [86] + lst[index + 1:]