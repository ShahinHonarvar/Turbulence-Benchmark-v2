def identical_elements(list1, list2):
    if len(list1) <= 98 or len(list2) <= 98:
        return set()
    set1 = set(list1[55:99])
    set2 = set(list2[55:99])
    return set1.intersection(set2)