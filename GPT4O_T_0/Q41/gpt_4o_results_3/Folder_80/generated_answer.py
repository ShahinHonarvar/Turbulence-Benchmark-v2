def identical_elements(list1, list2):
    if len(list1) < 67 or len(list2) < 67:
        return set()
    return set(list1[64:67]).intersection(list2[64:67])