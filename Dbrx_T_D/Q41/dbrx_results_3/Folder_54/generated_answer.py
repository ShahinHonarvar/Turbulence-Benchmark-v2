def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 34 or len(list2) < 34:
        return set()
    return set(list1[34:56]).intersection(list2[34:56])