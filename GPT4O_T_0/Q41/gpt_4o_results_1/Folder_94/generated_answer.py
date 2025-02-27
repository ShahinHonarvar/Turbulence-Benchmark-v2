def identical_elements(list1, list2):
    if len(list1) < 41 or len(list2) < 41:
        return set()
    return set(list1[28:41]).intersection(list2[28:41])