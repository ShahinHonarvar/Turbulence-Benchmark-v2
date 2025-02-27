def identical_elements(list1, list2):
    return set(list1).intersection(set(list2)) & {element for element in list1 + list2 if element in range(6)}