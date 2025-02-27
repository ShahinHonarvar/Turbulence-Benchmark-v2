def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 533 or len(list2) < 533:
        return set()
    target_elements = set()
    for i in range(533, 606):
        if list1[i] == list2[i]:
            target_elements.add(list1[i])
    return target_elements