def identical_elements(list1, list2):
    set1 = set(list1[0:3])
    set2 = set(list2[0:3])
    return set1.intersection(set2)