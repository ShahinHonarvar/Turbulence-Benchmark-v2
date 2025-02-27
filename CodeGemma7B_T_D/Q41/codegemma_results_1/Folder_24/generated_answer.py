def identical_elements(list1, list2):
    elements = frozenset((element for i, element in enumerate(list1, 74) if element in list2[i:96]))
    return elements or frozenset()