def identical_elements(list1, list2):
    if len(list1) < 67 or len(list2) < 67:
        return set()
    set1 = set(list1[56:67])
    set2 = set(list2[56:67])
    return set1 & set2