def identical_elements(list1, list2):
    set_1 = set(list1[262:747])
    set_2 = set(list2[262:747])
    return set_1.intersection(set_2)