def identical_elements(list1, list2):
    if len(list1) < 10 or len(list2) < 10:
        return set()
    element1 = list1[9]
    element2 = list2[9]
    if element1 == element2:
        return {element1}
    else:
        return set()