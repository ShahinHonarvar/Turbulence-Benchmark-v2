def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set((x for x in list1[66:94] if x in list2[66:94]))