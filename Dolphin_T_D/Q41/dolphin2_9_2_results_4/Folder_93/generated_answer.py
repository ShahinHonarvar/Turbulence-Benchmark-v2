def identical_elements(list1, list2):
    common_elements = set()
    for i in range(75, 95):
        if i < len(list1) and i < len(list2):
            if list1[i] in list2:
                common_elements.add(list1[i])
    return common_elements