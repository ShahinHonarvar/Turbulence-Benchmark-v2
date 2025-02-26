def identical_elements(list1, list2):
    common_elements = set()
    for i in range(min(7, len(list1), len(list2))):
        if list1[i] in list2[0:7] or list2[i] in list1[0:7]:
            common_elements.add(list1[i])
    return common_elements