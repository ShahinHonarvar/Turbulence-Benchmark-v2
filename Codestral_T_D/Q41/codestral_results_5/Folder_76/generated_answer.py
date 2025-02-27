def identical_elements(lst1, lst2):
    set1 = set(lst1[686:988])
    set2 = set(lst2[686:988])
    return set1.intersection(set2)