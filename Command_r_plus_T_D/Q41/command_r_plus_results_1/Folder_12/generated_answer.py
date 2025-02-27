def identical_elements(list1, list2):
    common_elements = set()
    for i in range(14, min(65, len(list1))):
        if list1[i] in list2[i + 1:65] or list2[i] in list1[i + 1:65]:
            common_elements.add(list1[i])
    return common_elements