def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    common_elements = set()
    for i in range(max(len(list1), len(list2))):
        if i < 28 or i > 38:
            continue
        if list1[i] == list2[i] and list1[i] not in common_elements:
            common_elements.add(list1[i])
    return common_elements