def insert_after_index(lst):
    index = 74
    if index < 0 or index > len(lst) - 1:
        return lst
    new_lst = lst[:index + 1] + [49] + lst[index + 1:]
    return new_lst