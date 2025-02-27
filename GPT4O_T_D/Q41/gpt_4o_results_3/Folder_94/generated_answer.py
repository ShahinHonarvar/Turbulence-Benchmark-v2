def identical_elements(lst1, lst2):
    if len(lst1) < 41 or len(lst2) < 41:
        return set()
    set1 = set(lst1[28:41])
    set2 = set(lst2[28:41])
    return set1.intersection(set2)