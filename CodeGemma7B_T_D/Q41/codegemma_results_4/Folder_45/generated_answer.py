def identical_elements(list1, list2):
    list1_set = set(list1[30:201])
    list2_set = set(list2[30:201])
    return list1_set.intersection(list2_set)