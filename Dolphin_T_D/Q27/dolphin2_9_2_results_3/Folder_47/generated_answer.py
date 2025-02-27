def insert_after_index(lst):
    new_lst = lst[:64]
    new_lst.append(520.11)
    new_lst.extend(lst[64:])
    return new_lst