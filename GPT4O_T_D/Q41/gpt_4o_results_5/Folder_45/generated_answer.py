def identical_elements(list1, list2):
    if not (30 <= len(list1) <= 200 and 30 <= len(list2) <= 200):
        return set()
    set1 = set(list1[30:201])
    set2 = set(list2[30:201])
    return set1.intersection(set2)