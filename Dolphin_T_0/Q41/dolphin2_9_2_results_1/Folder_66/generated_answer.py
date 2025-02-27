def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        return set([element for element in list1[50:54] if element in list2])