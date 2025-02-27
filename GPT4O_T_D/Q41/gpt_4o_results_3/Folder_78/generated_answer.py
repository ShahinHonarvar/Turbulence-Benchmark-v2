def identical_elements(list1, list2):
    if len(list1) < 52 or len(list2) < 52:
        return set()
    return set(list1[43:52]) & set(list2[43:52])