def identical_elements(list1, list2):
    set1 = set(list1[10:100])
    set2 = set(list2[10:100])
    return set1.intersection(set2)