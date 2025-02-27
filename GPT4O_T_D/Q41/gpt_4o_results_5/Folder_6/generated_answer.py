def identical_elements(list1, list2):
    if len(list1) < 67 or len(list2) < 67:
        return set()
    elements_list1 = set(list1[10:67])
    elements_list2 = set(list2[10:67])
    return elements_list1.intersection(elements_list2)