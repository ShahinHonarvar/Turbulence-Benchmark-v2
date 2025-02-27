def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same size')
    if len(list1) < 30 or len(list1) > 87:
        return set()
    common_elements = set()
    for i in range(30, 88):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements