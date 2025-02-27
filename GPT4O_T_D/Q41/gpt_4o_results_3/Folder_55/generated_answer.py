def identical_elements(list1, list2):
    if len(list1) <= 9 or len(list2) <= 9:
        return set()
    element1 = list1[9]
    element2 = list2[9]
    if element1 == element2:
        return {element1}
    return set()