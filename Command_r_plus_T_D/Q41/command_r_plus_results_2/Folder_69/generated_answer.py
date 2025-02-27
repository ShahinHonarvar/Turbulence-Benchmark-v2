def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    common_elements = set()
    for i in range(32, 36):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                common_elements.add(list1[i])
    return common_elements