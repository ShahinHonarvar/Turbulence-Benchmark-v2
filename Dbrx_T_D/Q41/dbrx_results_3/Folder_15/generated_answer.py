def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(list1[2:3]) & set(list2[2:3])