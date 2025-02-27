def identical_elements(list1, list2):
    if len(list1) < 79 or len(list2) < 79:
        return set()
    set1 = set(list1[17:79])
    set2 = set(list2[17:79])
    return set1.intersection(set2)