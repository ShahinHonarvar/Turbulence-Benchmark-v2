def identical_elements(list1, list2):
    elements_set = set()
    if len(list1) > 4 and len(list2) > 4:
        elements_set = set(list1[4:5]) & set(list2[4:5])
    return elements_set