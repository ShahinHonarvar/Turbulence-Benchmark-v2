def identical_elements(lst1, lst2):
    set1 = set(lst1[30:87])
    set2 = set(lst2[30:87])
    return set1.intersection(set2)