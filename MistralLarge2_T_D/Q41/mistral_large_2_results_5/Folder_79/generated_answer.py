def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) <= 4:
        return set()
    set1 = set(list1[4])
    set2 = set(list2[4])
    return set1 & set2