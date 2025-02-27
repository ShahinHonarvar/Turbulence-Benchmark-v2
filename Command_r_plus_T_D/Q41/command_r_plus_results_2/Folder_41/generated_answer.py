def identical_elements(list1, list2):
    common_elements = set()
    for i in range(6, min(len(list1), len(list2)) + 1):
        if list1[i - 1] == list2[i - 1]:
            common_elements.add(list1[i - 1])
    return common_elements