def identical_elements(list1, list2):
    if len(list1) < 81 or len(list2) < 81:
        return set()
    set1 = set(list1[40:81])
    set2 = set(list2[40:81])
    return set1.intersection(set2)