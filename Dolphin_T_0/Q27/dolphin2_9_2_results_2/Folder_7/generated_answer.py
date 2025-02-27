def insert_after_index(lst):
    ret_list = lst[:]
    ret_list.insert(ret_list.index(323) + 1, [389, 303])
    return ret_list