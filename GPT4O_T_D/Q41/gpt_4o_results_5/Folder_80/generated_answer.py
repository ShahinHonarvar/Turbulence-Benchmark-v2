def identical_elements(list1, list2):
    if len(list1) <= 66 or len(list2) <= 66:
        return set()
    set1 = set(list1[64:67])
    set2 = set(list2[64:67])
    return set1.intersection(set2)