def identical_elements(list1, list2):
    if len(list1) < 56 or len(list2) < 56:
        return set()
    set1 = set(list1[27:56])
    set2 = set(list2[27:56])
    return set1.intersection(set2)