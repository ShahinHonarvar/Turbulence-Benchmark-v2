def identical_elements(list1, list2):
    set1 = set(list1[29:94])
    set2 = set(list2[29:94])
    return set1.intersection(set2)