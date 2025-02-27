def identical_elements(list1, list2):
    if len(list1) <= 36 or len(list2) <= 36:
        return set()
    return set(list1[33:37]) & set(list2[33:37])