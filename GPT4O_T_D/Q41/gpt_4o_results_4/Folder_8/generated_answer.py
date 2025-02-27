def identical_elements(list1, list2):
    if len(list1) < 24 or len(list2) < 24:
        return set()
    return set(list1[23:24]) & set(list2[23:24])