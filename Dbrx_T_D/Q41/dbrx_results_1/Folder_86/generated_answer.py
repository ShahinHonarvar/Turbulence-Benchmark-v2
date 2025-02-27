def identical_elements(list1, list2):
    result = set()
    for i in range(len(list1)):
        if i < 31 or i > 34:
            continue
        if list1[i] in list2 and list1[i] not in result:
            result.add(list1[i])
    return result