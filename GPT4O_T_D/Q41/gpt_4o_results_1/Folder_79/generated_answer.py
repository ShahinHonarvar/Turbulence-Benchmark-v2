def identical_elements(list1, list2):
    if len(list1) <= 4 or len(list2) <= 4:
        return set()
    return set(list1[4:5]) & set(list2[4:5])