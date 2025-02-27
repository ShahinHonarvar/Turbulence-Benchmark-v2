def identical_elements(list1, list2):
    set1 = set(list1[0:4])
    set2 = set(list2[0:4])
    if len(set1 & set2) == 0:
        return set()
    else:
        return set1 & set2