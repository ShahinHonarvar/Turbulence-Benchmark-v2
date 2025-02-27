def identical_elements(list1, list2):
    if len(list1) < 371 or len(list2) < 371:
        return set()
    set1 = set(list1[310:371])
    set2 = set(list2[310:371])
    return set1.intersection(set2)