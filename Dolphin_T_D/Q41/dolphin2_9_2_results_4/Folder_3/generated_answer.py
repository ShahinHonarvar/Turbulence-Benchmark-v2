def identical_elements(list1, list2):
    set_list1 = set(list1[62:92])
    set_list2 = set(list2[62:92])
    return set_list1.intersection(set_list2)