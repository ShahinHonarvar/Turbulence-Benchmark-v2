def identical_elements(list1, list2):
    if len(list1) < 53 or len(list2) < 53:
        return set()
    set1 = set(list1[26:53])
    set2 = set(list2[26:53])
    return set1.intersection(set2)