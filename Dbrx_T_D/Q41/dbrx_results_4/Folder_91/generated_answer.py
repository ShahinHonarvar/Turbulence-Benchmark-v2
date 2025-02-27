def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 5:
        return set()
    else:
        return set(list1[:5]) & set(list2[:5])