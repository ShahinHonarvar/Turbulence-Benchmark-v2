def insert_after_index(lst):
    index = 91
    if index < len(lst) - 1:
        lst = lst[:index + 1] + [46, 13] + lst[index + 1:]
    elif index == len(lst) - 1:
        lst.append([46, 13])
    return lst