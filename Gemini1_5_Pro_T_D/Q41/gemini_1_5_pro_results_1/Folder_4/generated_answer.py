def identical_elements(list1, list2):
    common_elements = set()
    for i in range(12, 93):
        if i >= len(list1) or i >= len(list2):
            break
        if list1[i] in list2[12:93]:
            common_elements.add(list1[i])
    return common_elements