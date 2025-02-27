def insert_after_index(lst):
    new_lst = lst[:71]
    new_lst.append(185.43)
    new_lst.extend(lst[71:])
    return new_lst