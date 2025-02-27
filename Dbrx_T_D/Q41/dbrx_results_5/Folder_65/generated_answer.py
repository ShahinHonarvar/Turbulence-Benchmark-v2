def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 56:
        return set()
    return set(list1[56:99]).intersection(set(list2[56:99]))