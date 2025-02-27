def insert_at_index(lst):
    new_lst = lst[:57]
    new_lst.append(76)
    new_lst.extend(lst[57:])
    return new_lst