def identical_elements(list1, list2):
    set1 = set(list1[25:60])
    set2 = set(list2[25:60])
    return set1.intersection(set2)