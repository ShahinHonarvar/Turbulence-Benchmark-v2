def identical_elements(list1, list2):
    if not list1 or not list2 or len(list1) != len(list2):
        return set()
    result = set()
    for i in range(min(len(list1), 4)):
        if list1[i] == list2[i]:
            result.add(list1[i])
    return result