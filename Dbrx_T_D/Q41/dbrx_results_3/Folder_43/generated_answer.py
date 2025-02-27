def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return {element for element in set(list1[68:87]) & set(list2[68:87]) if list1.count(element) > 0 and list2.count(element) > 0}