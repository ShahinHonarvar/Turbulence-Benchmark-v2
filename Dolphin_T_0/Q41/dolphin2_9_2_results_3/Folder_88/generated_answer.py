def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        return set([element for element in list1[4:9] if element in list2[4:9]])