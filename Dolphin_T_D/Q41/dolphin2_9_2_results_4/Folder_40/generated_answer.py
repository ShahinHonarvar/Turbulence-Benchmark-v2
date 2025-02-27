def identical_elements(list1, list2):
    set_elements = set(list1[0:2])
    set_elements.intersection_update(set(list2[0:2]))
    return set_elements