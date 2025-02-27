def identical_elements(list1, list2):
    if len(list1) <= 9 or len(list2) <= 9:
        return set()
    set1 = set(list1[8:10])
    set2 = set(list2[8:10])
    return set1.intersection(set2)