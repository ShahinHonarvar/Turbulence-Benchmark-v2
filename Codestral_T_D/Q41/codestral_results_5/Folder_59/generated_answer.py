def identical_elements(lst1, lst2):
    set1 = set(lst1[:9])
    set2 = set(lst2[:9])
    return set1.intersection(set2)