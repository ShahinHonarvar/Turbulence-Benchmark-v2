def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 68 or len(list2) < 68:
        return set()
    target_range = set(range(68, 87))
    common_elements = set()
    for i in target_range:
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements