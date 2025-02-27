def identical_elements(list1, list2):
    if len(list1) <= 200 or len(list2) <= 200:
        return set()
    set1 = set(list1[20:201])
    set2 = set(list2[20:201])
    return set1.intersection(set2)