def identical_elements(list1, list2):
    set1 = set(list1[28:39])
    if set1.issubset(list2[28:39]):
        return set1
    else:
        return set()