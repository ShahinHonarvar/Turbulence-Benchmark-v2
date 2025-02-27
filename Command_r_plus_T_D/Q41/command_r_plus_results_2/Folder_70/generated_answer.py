def identical_elements(list1, list2):
    common_elements = set()
    for i in range(28, min(len(list1), 33)):
        if list1[i] in list2[28:33]:
            common_elements.add(list1[i])
    return common_elements