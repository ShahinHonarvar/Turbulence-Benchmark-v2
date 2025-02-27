def identical_elements(list1, list2):
    if len(list1) < 6 or len(list2) < 6:
        return set()
    return set(list1[3:6]).intersection(set(list2[3:6]))