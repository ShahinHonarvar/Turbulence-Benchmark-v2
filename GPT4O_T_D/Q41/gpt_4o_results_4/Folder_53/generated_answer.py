def identical_elements(list1, list2):
    if len(list1) > 200 and len(list2) > 200:
        set1 = set(list1[200:201])
        set2 = set(list2[200:201])
        return set1 & set2
    return set()