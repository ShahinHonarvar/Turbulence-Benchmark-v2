def insert_after_index(lst):
    index = 35
    if index < 0 or index > len(lst) - 1:
        return 'Error: Index out of range'
    new_lst = lst[:index + 1] + [88] + lst[index + 1:]
    return new_lst