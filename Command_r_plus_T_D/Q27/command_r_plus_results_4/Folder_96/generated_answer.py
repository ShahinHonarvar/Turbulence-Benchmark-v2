def insert_after_index(lst):
    index = 74
    new_lst = lst[:index + 1] + [51, 29] + lst[index + 1:]
    return new_lst