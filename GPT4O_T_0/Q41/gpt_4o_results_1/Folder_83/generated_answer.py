def identical_elements(list1, list2):
    if len(list1) < 201 or len(list2) < 201:
        return set()
    set1 = set(list1[90:201])
    set2 = set(list2[90:201])
    return set1.intersection(set2)