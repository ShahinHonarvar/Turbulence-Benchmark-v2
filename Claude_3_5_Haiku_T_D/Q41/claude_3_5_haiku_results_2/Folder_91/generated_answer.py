def identical_elements(list1, list2):
    elements = set(list1[:5]) & set(list2[:5])
    return elements