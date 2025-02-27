def identical_elements(list1, list2):
    if len(list1) > 9 and len(list2) > 9:
        set1 = set([list1[9]])
        set2 = set([list2[9]])
        return set1.intersection(set2)
    return set()