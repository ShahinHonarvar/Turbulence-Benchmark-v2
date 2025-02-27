def identical_elements(list1, list2):
    if len(list1) < 99 or len(list2) < 99:
        return set()
    return set(list1[55:99]).intersection(set(list2[55:99]))