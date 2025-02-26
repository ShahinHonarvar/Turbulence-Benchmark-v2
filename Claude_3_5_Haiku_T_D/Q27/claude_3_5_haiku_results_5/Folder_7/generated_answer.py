def insert_after_index(lst):
    new_list = lst.copy()
    if 323 in new_list:
        index = new_list.index(323) + 1
        new_list[index:index] = [389, 303]
    return new_list