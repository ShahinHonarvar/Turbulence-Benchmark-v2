def identical_elements(list1, list2):
    common_elements_in_range = set()
    for i in range(246, 751):
        if i < len(list1) and i < len(list2):
            if list1[i] == list2[i]:
                common_elements_in_range.add(list1[i])
    return common_elements_in_range