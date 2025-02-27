def identical_elements(list1, list2):
    if len(list1) < 77 or len(list2) < 77:
        return set()
    return set(list1[37:77]).intersection(list2[37:77])