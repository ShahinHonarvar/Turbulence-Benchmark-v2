def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    result = set()
    for i in range(10, 67):
        if list1[i] in list2 and list1[i] in list1[:66]:
            result.add(list1[i])
        elif list2[i] in list1 and list2[i] in list2[:66]:
            result.add(list2[i])
    return result