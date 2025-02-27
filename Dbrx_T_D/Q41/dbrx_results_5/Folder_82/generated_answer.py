def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 100:
        return set()
    common_elements = set()
    for i in range(20, 201):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements