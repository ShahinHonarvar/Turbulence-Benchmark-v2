def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 201:
        return set()
    set1 = set(list1[30:201])
    set2 = set(list2[30:201])
    return set1.intersection(set2)