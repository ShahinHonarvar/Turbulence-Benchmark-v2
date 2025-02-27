def identical_elements(list1, list2):
    if len(list1) == len(list2) and 28 <= len(list1) <= 38:
        return set(list1[28:39]) & set(list2[28:39])
    return set()