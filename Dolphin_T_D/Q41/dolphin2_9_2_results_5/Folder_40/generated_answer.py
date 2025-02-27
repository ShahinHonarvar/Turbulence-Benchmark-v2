def identical_elements(list1, list2):
    set1 = set(list1[0:2])
    set2 = set(list2[0:2])
    if set1.intersection(set2):
        return set1.intersection(set2)
    else:
        return set()