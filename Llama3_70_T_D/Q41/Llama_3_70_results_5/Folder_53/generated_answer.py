def identical_elements(list1, list2):
    set1 = set(list1[0:201])
    set2 = set(list2[0:201])
    return set1.intersection(set2)