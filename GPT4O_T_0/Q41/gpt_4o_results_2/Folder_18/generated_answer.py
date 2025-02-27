def identical_elements(list1, list2):
    if len(list1) < 50 or len(list2) < 50:
        return set()
    set1 = set(list1[35:50])
    set2 = set(list2[35:50])
    return set1.intersection(set2)