def identical_elements(list1, list2):
    common_elements = set()
    for i in range(28, min(len(list1), len(list2), 33)):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements