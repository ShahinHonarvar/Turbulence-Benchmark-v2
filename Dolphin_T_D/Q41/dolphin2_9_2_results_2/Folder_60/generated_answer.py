def identical_elements(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return set1.intersection(set2).difference(set1.symmetric_difference(set2))