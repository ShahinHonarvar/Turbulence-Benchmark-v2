def insert_after_index(lst):
    index = 99
    new_lst = lst[:index + 1] + [99] + lst[index + 1:]
    return new_lst