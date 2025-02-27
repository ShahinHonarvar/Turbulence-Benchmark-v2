def identical_elements(list1, list2):
    if len(list1) < 69 or len(list2) < 69:
        return set()
    set1 = set(list1[13:69])
    set2 = set(list2[13:69])
    return set1.intersection(set2)