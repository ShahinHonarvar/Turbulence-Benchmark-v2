def identical_elements(list1, list2):
    return set([element for i, element in enumerate(list1[2:3]) for j, other_element in enumerate(list2[2:3]) if element == other_element])