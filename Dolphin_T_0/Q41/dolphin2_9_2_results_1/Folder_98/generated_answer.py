def identical_elements(list1, list2):
    set1 = set(list1[0:6])
    set2 = set(list2[0:6])
    return set1.intersection(set2)