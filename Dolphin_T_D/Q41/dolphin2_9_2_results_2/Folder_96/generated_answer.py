def identical_elements(list1, list2):
    common_elements = set()
    for i in range(200, 501):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    if len(common_elements) == 0:
        return set()
    else:
        return common_elements