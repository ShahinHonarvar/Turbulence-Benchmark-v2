def identical_elements(list1, list2):
    if len(list1) < 72 or len(list2) < 72:
        return set()
    set1 = set(list1[52:72])
    set2 = set(list2[52:72])
    return set1.intersection(set2)