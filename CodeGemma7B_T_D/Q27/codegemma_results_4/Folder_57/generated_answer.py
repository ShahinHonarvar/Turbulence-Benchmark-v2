def insert_after_index(lst):
    index = 90
    new_lst = lst[:index + 1]
    new_lst.append(80)
    new_lst.extend(lst[index + 1:])
    return new_lst