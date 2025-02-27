def identical_elements(lst1, lst2):
    set1 = set(lst1[6:9])
    set2 = set(lst2[6:9])
    return set1 & set2 if set1 and set2 else set()