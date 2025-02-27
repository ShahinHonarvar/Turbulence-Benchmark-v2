def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 6:
        return set()
    return set(list1[1:6]).intersection(list2[1:6])