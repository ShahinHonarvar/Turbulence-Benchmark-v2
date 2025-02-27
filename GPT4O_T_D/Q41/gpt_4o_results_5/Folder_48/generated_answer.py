def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 606:
        return set()
    set1 = set(list1[533:606])
    set2 = set(list2[533:606])
    return set1.intersection(set2)