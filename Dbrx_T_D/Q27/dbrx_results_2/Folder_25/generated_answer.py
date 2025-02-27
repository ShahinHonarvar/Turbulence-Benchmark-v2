def insert_after_index(lst):
    index_30 = 30
    if index_30 >= len(lst):
        return lst
    else:
        new_lst = lst[:index_30 + 1] + [37] + lst[index_30 + 1:]
        return new_lst