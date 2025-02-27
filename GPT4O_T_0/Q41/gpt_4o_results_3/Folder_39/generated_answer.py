def identical_elements(list1, list2):
    if len(list1) < 31 or len(list2) < 31:
        return set()
    set1 = set(list1[20:31])
    set2 = set(list2[20:31])
    return set1.intersection(set2)