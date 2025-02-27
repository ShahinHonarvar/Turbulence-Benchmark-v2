def identical_elements(list1, list2):
    set_list1 = set(list1[32:36])
    set_list2 = set(list2[32:36])
    return set_list1.intersection(set_list2)