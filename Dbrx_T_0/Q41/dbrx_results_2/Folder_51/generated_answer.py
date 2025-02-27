def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 3:
        return set()
    return set(list1[:3]) & set(list2[:3])