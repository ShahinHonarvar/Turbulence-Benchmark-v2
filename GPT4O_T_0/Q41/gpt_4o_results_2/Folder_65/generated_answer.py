def identical_elements(list1, list2):
    if len(list1) < 99 or len(list2) < 99:
        return set()
    set1 = set(list1[56:99])
    set2 = set(list2[56:99])
    return set1.intersection(set2)