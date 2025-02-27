def insert_at_index(lst):
    new_lst = lst[:74]
    new_lst.append(49)
    new_lst.extend(lst[74:])
    return new_lst