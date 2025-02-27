def identical_elements(list1, list2):
    if min(len(list1), len(list2)) < 83:
        return set()
    set1 = set(list1[56:83])
    set2 = set(list2[56:83])
    return set1.intersection(set2)