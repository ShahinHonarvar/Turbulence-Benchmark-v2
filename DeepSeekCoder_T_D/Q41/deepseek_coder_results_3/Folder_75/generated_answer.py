def identical_elements(list1, list2):
    if len(list1) == len(list2) and len(list1) > 57:
        return set(list1[56:58]) & set(list2[56:58])
    return set()