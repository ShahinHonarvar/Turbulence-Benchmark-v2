def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size.')
    shared_elements = set()
    for i in range(60, 201):
        if i < len(list1):
            if list1[i] in list2[60:201]:
                shared_elements.add(list1[i])
            if list2[i] in list1[60:201]:
                shared_elements.add(list2[i])
    return shared_elements