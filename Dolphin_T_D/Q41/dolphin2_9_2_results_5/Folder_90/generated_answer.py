def identical_elements(lst1, lst2):
    set1 = set(lst1[262:747])
    set2 = set(lst2[262:747])
    return set1.intersection(set2)