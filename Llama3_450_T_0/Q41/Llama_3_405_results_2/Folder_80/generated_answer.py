def identical_elements(list1, list2):
    set1 = set(list1[64:67])
    set2 = set(list2[64:67])
    return set1.intersection(set2)