def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 30 or len(list2) < 30:
        return set()
    result = set()
    for i in range(30, 88):
        if list1[i] in list2 and list1[i] not in result:
            result.add(list1[i])
        if list2[i] in list1 and list2[i] not in result:
            result.add(list2[i])
    return result