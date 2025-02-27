def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 6:
        return set()
    else:
        return set(list1[:6]) & set(list2[:6])