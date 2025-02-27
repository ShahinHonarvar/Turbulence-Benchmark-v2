def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    result = set()
    for i in range(2, len(list1)):
        if list1[i] == list2[i] and list1[i] not in result:
            result.add(list1[i])
    return result