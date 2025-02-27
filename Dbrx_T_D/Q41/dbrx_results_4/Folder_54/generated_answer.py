def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        common_elements = set()
        for i in range(34, 56):
            if list1[i] in list2 and list1[i] not in common_elements:
                common_elements.add(list1[i])
            if list2[i] in list1 and list2[i] not in common_elements:
                common_elements.add(list2[i])
        return common_elements