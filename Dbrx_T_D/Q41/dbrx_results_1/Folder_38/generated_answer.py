def identical_elements(list1, list2):
    elements = set()
    for i in range(len(list1)):
        if i >= 22 and i <= 63 and (list1[i] == list2[i]):
            elements.add(list1[i])
    return elements