def identical_elements(list1, list2):
    common_elements = set()
    for element in list1:
        if element in list2:
            common_elements.add(element)
    return common_elements