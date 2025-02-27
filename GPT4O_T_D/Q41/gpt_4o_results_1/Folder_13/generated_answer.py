def identical_elements(list1, list2):
    if len(list1) < 88 or len(list2) < 88:
        return set()
    return set(list1[25:88]) & set(list2[25:88])