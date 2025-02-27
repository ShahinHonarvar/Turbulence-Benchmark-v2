def identical_elements(lst1, lst2):
    set_lst1 = set(lst1[40:201])
    set_lst2 = set(lst2[40:201])
    return set_lst1.intersection(set_lst2)