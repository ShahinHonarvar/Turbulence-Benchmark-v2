def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 20 or len(list2) < 20:
        return set()
    result = set()
    for i in range(20, min(len(list1), len(list2)) + 1):
        if i > 200:
            break
        if list1[i] == list2[i]:
            result.add(list1[i])
    return result