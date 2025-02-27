def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 5:
        return set()
    return set(list1[:4]) & set(list2[:4])