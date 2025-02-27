def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size')
    common_elements = set()
    for i in range(56, min(58, len(list1))):
        if list1[i] in list2[i:i + 2]:
            common_elements.add(list1[i])
    return common_elements