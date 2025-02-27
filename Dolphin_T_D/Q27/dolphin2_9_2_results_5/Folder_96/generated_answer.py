def insert_after_index(lst):
    new_list = lst[:74]
    new_list.extend([51, 29])
    new_list.extend(lst[74:])
    return new_list