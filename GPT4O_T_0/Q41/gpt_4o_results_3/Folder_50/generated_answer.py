def identical_elements(list1, list2):
    if len(list1) < 85 or len(list2) < 85:
        return set()
    set1 = set(list1[70:85])
    set2 = set(list2[70:85])
    return set1.intersection(set2)