def insert_after_index(lst):
    new_lst = lst[:370]
    new_lst.append(285.4)
    new_lst += lst[370:]
    return new_lst