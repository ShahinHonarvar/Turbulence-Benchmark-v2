def identical_elements(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)) or len(list1) != len(list2):
        raise ValueError('Both arguments must be lists of the same size')
    common_elements = set()
    for i in range(310, 371):
        if list1[i] in list2[i] and list1[i] not in common_elements:
            common_elements.add(list1[i])
    return common_elements