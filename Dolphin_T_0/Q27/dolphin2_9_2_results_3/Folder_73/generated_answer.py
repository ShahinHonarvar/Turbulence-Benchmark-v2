def insert_after_index(lst):
    index = lst.index(87)
    new_lst = lst[:index + 1] + [637.22] + lst[index + 1:]
    return new_lst