def insert_at_index(lst):
    new_lst = lst[:85]
    new_lst.append(27)
    new_lst.extend(lst[85:])
    return new_lst