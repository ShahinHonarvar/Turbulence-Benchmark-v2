def identical_elements(list1, list2):
    set1 = set(list1[:8])
    set2 = set(list2[:8])
    return set1.intersection(set2)