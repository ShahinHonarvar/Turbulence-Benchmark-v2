def identical_elements(list1, list2):
    if len(list1) < 9 or len(list2) < 9:
        return set()
    set1 = set(list1[6:9])
    set2 = set(list2[6:9])
    return set1 & set2