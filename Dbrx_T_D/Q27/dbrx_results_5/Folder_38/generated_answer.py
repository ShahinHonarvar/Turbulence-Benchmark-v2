def insert_after_index(lst):
    index = 89
    while index + 1 < len(lst) and lst[index + 1] < lst[index]:
        index += 1
    lst = lst[:index + 1] + [86] + lst[index + 1:]
    return lst