def identical_elements(list1, list2):
    if len(list1) < 36 or len(list2) < 36:
        return set()
    return set(list1[32:36]).intersection(list2[32:36])