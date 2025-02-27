def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(list1[17:79]) & set(list2[17:79])