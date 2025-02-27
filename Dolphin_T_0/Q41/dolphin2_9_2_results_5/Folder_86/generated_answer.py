def identical_elements(lst1, lst2):
    set1 = set(lst1[31:35])
    set2 = set(lst2[31:35])
    return set1.intersection(set2)