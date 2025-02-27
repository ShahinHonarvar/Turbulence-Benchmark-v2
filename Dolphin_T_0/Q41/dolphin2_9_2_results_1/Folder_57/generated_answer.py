def identical_elements(list1, list2):
    elements = set()
    for i in range(min(27, len(list1)), min(56, len(list2)) + 1):
        if list1[i] == list2[i]:
            elements.add(list1[i])
    return elements