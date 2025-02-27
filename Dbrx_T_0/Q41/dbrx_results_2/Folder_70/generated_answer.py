def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    result = set()
    for i in range(28, 33):
        if list1[i] in list2[i:33] + list2[0:i]:
            result.add(list1[i])
    return result