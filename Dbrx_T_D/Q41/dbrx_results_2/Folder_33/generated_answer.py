def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists should be of the same size')
    elements = set()
    for i in range(667, 775):
        if list1[i] in list2[667:774] and list1[i] not in elements:
            elements.add(list1[i])
    return elements