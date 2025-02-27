def insert_at_index(lst):
    new_lst = []
    new_lst.extend(lst[:761])
    new_lst.append(925)
    new_lst.extend(lst[761:])
    return new_lst