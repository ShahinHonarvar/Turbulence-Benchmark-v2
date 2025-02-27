def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 2:
        return set()
    return set(list1[:2]).intersection(list2[:2])