def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    target_elements = set()
    for i in range(52, 72):
        if list1[i] in target_elements or list2[i] in target_elements:
            continue
        if list1[i] == list2[i]:
            target_elements.add(list1[i])
    return target_elements