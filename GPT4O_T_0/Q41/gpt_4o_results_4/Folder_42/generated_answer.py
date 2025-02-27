def identical_elements(list1, list2):
    if len(list1) < 80 or len(list2) < 80:
        return set()
    set1 = set(list1[29:80])
    set2 = set(list2[29:80])
    return set1.intersection(set2)