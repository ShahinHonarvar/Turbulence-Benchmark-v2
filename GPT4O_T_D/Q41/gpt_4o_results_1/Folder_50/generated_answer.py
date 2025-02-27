def identical_elements(list1, list2):
    if len(list1) < 85 or len(list2) < 85:
        return set()
    subset1 = set(list1[70:85])
    subset2 = set(list2[70:85])
    return subset1.intersection(subset2)