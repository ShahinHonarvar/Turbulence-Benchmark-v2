def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(list1[56:83]) & set(list2[56:83])