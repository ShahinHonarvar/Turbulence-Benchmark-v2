def insert_after_index(lst):
    index = 183
    insertion = [148, 145]
    if index < 0 or index > len(lst) - 1:
        return lst
    else:
        new_lst = lst[:index + 1] + insertion + lst[index + 1:]
        return new_lst