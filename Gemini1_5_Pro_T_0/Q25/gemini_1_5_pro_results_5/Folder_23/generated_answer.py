def insert_at_index(lst):
    new_lst = lst[:38]
    new_lst.append(45)
    new_lst.extend(lst[38:])
    return new_lst