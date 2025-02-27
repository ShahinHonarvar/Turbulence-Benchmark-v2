def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    result = set()
    for i in range(max(len(list1), len(list2))):
        if i in range(28, 33) and list1[i] == list2[i]:
            result.add(list1[i])
    return result