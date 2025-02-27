def insert_after_index(lst, index):
    if index < 0 or index >= len(lst):
        return lst
    else:
        new_lst = lst[:index + 1] + [149] + lst[index + 1:]
        return new_lst