def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    result = set()
    for i in range(10, 101):
        if list1[i] == list2[i]:
            if list1[i] not in result:
                result.add(list1[i])
    return result