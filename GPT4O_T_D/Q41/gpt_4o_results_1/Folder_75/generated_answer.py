def identical_elements(list1, list2):
    if len(list1) < 58 or len(list2) < 58:
        return set()
    return set(list1[56:58]) & set(list2[56:58])