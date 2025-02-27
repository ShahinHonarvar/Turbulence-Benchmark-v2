def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be the same size')
    result = set()
    for i in range(50, 55):
        if list1[i] == list2[i]:
            result.add(list1[i])
    return result