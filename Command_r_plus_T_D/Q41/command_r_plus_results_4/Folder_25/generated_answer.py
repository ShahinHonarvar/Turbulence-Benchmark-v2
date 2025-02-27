def identical_elements(list1, list2):
    common_elements = set()
    for i in range(29, min(94, len(list1))):
        if list1[i] in list2[29:94]:
            common_elements.add(list1[i])
    return common_elements