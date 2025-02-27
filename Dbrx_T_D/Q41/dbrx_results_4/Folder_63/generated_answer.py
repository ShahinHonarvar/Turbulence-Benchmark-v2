def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 22 or len(list2) < 22:
        return set()
    return set(list1[22:89]).intersection(list2[22:89])