def identical_elements(list1, list2):
    common_set = set()
    for i in range(min(70, len(list1)), min(201, len(list1))):
        if list1[i] in list2[min(70, len(list2)):min(201, len(list2))]:
            common_set.add(list1[i])
    return common_set