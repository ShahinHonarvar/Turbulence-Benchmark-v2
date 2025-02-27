def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    identical = set()
    for i in range(31, 35):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                identical.add(list1[i])
    return identical