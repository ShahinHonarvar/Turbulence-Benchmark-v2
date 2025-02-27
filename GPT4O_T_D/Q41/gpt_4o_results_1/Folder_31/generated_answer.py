def identical_elements(list1, list2):
    if len(list1) <= 88 or len(list2) <= 88:
        return set()
    set1 = set(list1[75:89])
    set2 = set(list2[75:89])
    return set1.intersection(set2)