def identical_elements(list1, list2):
    if len(list1) == len(list2) and 68 <= len(list1) <= 86:
        return set(list1[68:87]) & set(list2[68:87])
    else:
        return set()