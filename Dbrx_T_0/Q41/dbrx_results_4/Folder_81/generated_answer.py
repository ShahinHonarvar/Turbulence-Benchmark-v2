def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 11 or len(list1) > 100:
        return set()
    return set(list1[10:101]) & set(list2[10:101])