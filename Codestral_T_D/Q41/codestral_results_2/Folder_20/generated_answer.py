def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 67:
        return set()
    return set(list1[56:67]) & set(list2[56:67])