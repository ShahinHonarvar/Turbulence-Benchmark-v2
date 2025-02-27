def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    result = set()
    for i in range(max(17, len(list1) - 78), min(len(list1) - 17, 78) + 1):
        if list1[i] in list2 and list1[i] not in result:
            result.add(list1[i])
    return result