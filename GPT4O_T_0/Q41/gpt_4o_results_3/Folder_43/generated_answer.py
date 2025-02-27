def identical_elements(list1, list2):
    if len(list1) < 87 or len(list2) < 87:
        return set()
    return set(list1[68:87]).intersection(list2[68:87])