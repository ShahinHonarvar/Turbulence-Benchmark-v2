def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 31:
        return set()
    return set(list1[20:31]) & set(list2[20:31])