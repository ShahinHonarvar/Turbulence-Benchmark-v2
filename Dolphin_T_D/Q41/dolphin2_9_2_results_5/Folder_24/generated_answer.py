def identical_elements(list1, list2):
    common_elements = set()
    if len(list1) > 95 or len(list2) > 95:
        for i in range(74, min(len(list1), len(list2), 96)):
            if list1[i] == list2[i]:
                common_elements.add(list1[i])
    return common_elements