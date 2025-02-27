def identical_elements(list1, list2):
    if len(list1) < 93 or len(list2) < 93:
        return set()
    set1 = set(list1[62:93])
    set2 = set(list2[62:93])
    return set1.intersection(set2)