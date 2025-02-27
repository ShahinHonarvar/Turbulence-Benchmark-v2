def identical_elements(list1, list2):
    if len(list1) < 47 or len(list2) < 47:
        return set()
    set1 = set(list1[36:47])
    set2 = set(list2[36:47])
    return set1.intersection(set2)