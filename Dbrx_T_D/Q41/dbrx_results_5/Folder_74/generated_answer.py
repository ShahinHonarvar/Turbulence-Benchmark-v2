def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    result = set()
    for i in range(max(17, len(list1) - 78), min(len(list1) - 18, 78) + 1):
        if list1[i] == list2[i]:
            result.add(list1[i])
    return result