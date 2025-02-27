def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 24:
        return set()
    return set(list1[23:]).intersection(list2[23:])