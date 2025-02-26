def identical_elements(list1, list2):
    common_elements = set()
    for i in range(min(6, len(list1), len(list2))):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
        if list1[i] in list2[:i + 1] or list2[i] in list1[:i + 1]:
            common_elements.add(list1[i])
    return common_elements