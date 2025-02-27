def insert_after_index(lst):
    new_lst = lst[:29]
    new_lst.append(20)
    new_lst += lst[29:]
    return new_lst