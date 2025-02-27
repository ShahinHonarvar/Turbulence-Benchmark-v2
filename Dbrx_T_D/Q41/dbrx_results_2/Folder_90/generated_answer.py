def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 262 or len(list1) > 746:
        return set()
    return set(list1[262:747]) & set(list2[262:747])