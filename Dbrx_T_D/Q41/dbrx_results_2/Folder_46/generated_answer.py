def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 30 or len(list1) > 87:
        return set()
    return set(list1[30:88]) & set(list2[30:88])