def identical_elements(list1, list2):
    if len(list1) < 94 or len(list2) < 94:
        return set()
    set1 = set(list1[66:94])
    set2 = set(list2[66:94])
    return set1.intersection(set2)