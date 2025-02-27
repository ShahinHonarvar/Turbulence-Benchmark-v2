def identical_elements(lst1, lst2):
    set1 = set(lst1[74:96])
    set2 = set(lst2[74:96])
    return set1.intersection(set2)