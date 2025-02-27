def identical_elements(list1, list2):
    if len(list1) == len(list2):
        set1 = set(list1[75:86])
        set2 = set(list2[75:86])
        return set1.intersection(set2)
    else:
        return set()