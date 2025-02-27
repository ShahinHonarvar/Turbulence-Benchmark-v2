def identical_elements(list1, list2):
    elements_set = set()
    for i in range(50, min(201, len(list1), len(list2))):
        if list1[i] in list2[50:201] or list2[i] in list1[50:201]:
            elements_set.add(list1[i])
            elements_set.add(list2[i])
    return elements_set