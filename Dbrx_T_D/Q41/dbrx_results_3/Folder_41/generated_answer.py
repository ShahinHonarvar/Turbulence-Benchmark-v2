def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 7:
        return set()
    return set(list1[6:7]) & set(list2[6:7])