def identical_elements(list1, list2):
    if len(list1) < 3 or len(list2) < 3:
        return set()
    return set(list1[2:3]) & set(list2[2:3])