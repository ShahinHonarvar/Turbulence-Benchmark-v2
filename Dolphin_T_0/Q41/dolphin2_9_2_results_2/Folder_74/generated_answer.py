def identical_elements(lst1, lst2):
    set1 = set(lst1[17:79])
    set2 = set(lst2[17:79])
    return set1.intersection(set2)