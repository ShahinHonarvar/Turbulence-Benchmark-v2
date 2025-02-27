def identical_elements(list1, list2):
    if len(list1) < 40 or len(list2) < 40:
        return set()
    set1 = set(list1[15:40])
    set2 = set(list2[15:40])
    return set1.intersection(set2)