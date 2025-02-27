def identical_elements(list1, list2):
    if len(list1) < 49 or len(list2) < 49:
        return set()
    return set(list1[30:49]).intersection(list2[30:49])